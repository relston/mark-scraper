from playwright.sync_api import sync_playwright
import playwright
import re
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter
import playwright.sync_api
from .page import Page

class TimeoutError(Exception):
    pass
class BrowserError(Exception):
    pass

DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' + \
    ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.198 Safari/537.36'

def get(url: str) -> Page:
    raw_html = get_rendered_html(url)
    clean_soup = _clean_soup_from_html(raw_html)
    markdown = _markdown_from_soup(clean_soup)
    page = Page(url=url, body=markdown, html=raw_html)

    if title := clean_soup.find('title'):
        page.title = title.text

    return page

def get_rendered_html(url: str) -> str:
    try:
        return _render_page(url)
    except playwright.sync_api.Error as e:
        print(f"Error: {e}")
        raise BrowserError(f"BrowserError while fetching {url}")
    except playwright.sync_api.TimeoutError:
        raise TimeoutError(f"Timeout while fetching {url}")

def _render_page(url: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        # page.on('request', lambda request: print(f'Request: {request.url}'))
        # page.on('response', lambda response: print(f'Response: {response.url}'))
        # page.on('domcontentloaded', lambda page: print(f'domcontentloaded'))
        # page.on('load', lambda page: print(f'load'))
        page.goto(url, wait_until='load')
        page_content = page.content()
        
        frames = page.frames
        for frame in frames:
            if frame.url:
                page_content += frame.content()
        
        # page.screenshot(path="example.png")
        browser.close()
        return page_content

def _clean_soup_from_html(html: str) -> BeautifulSoup:
    # warnings.filterwarnings("ignore")

    soup = BeautifulSoup(html, 'html.parser')
    # List of tags to decompose
    tags_to_decompose = ['script', 'meta', 'link', 'style']

    for tag in soup.find_all(True):
        # Decompose unwanted tags
        if tag.name in tags_to_decompose:
            tag.decompose()
            continue
        
        if not tag.attrs:
            continue

        # Remove class attributes
        if 'class' in tag.attrs:
            del tag['class']

        # Remove style attributes
        if 'style' in tag.attrs:
            del tag['style']

    return soup


def _markdown_from_soup(soup: BeautifulSoup) -> str:
    raw_markdown_text = MarkdownConverter().convert_soup(soup)
    return re.sub(r'\n{3,}', '\n\n', raw_markdown_text)
