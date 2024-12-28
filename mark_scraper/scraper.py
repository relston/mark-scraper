import pyppeteer
import asyncio
import click
import re
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter
from .page import Page

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
        return asyncio.run(_render_page(url))
    except pyppeteer.errors.BrowserError:
        click.echo(f"BrowserError while fetching {url}", err=True)
        return None
    except pyppeteer.errors.TimeoutError:
        click.echo(f"Timeout while fetching {url}", err=True)
        return None

async def _render_page(url: str) -> str:
    browser = None
    try:
        browser = await pyppeteer.launch()
        page = await browser.newPage()
        await page.setUserAgent(DEFAULT_USER_AGENT)
        await page.goto(url)
        rendered_html = await page.content()
    finally:
        if browser:
            await browser.close()
    return rendered_html

def _clean_soup_from_html(html: str) -> BeautifulSoup:
    # warnings.filterwarnings("ignore")

    soup = BeautifulSoup(html, 'html.parser')

    # List of tags to decompose
    tags_to_decompose = ['script', 'meta', 'link', 'style']

    for tag in soup.find_all(True):
        # Remove class attributes
        if 'class' in tag.attrs:
            del tag['class']

        # Remove style attributes
        if 'style' in tag.attrs:
            del tag['style']

        # Decompose unwanted tags
        if tag.name in tags_to_decompose:
            tag.decompose()

    return soup


def _markdown_from_soup(soup: BeautifulSoup) -> str:
    raw_markdown_text = MarkdownConverter().convert_soup(soup)
    return re.sub(r'\n{3,}', '\n\n', raw_markdown_text)
