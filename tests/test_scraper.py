import pytest
import os
import re
from mark_scraper import scraper
from unittest.mock import patch

class TestScraper:
    @pytest.fixture
    def mock_web_page(self):
        url_to_content = {}

        def _mock(url, page_content):
            url_to_content[url] = page_content

        with patch('mark_scraper.scraper.get_rendered_html') as mock:
            def side_effect(url):
                return url_to_content[url]
            mock.side_effect = side_effect
            yield _mock

    def test_page_scrape(self, mock_web_page):
        """Basic python interface test"""

        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Basic HTML Page</title>
        </head>
        <body>
            <h1>Welcome to My Page</h1>
            <a href="https://www.example.com">Visit Example.com</a>
        </body>
        </html>
        """

        mock_web_page('https://supercool.com', html_content)

        page = scraper.get('https://supercool.com')

        assert page.title == 'Basic HTML Page'
        assert page.url == 'https://supercool.com'
        assert page.body == '\n\nBasic HTML Page\n\nWelcome to My Page\n' + \
            '==================\n\n[Visit Example.com](https://www.example.com)\n\n'

