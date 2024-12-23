import pytest
from textwrap import dedent
from mark_scraper import cli, Page
from unittest.mock import patch

class TestCLI:
    @pytest.fixture(autouse=True)
    def init(self):
        self.default_url = "http://example.com"

    @pytest.fixture
    def mock_stdout():
        with patch('click.echo') as mock:
            yield mock
    @pytest.fixture
    def mock_get_url(document_obj):
        with patch('mark_scraper.scraper.get') as mock:
            mock.return_value = document_obj
            yield mock

    def test_get_url(self, mock_stdout, mock_get_url):
        """Test CLI command with url"""
        
        # define the document object
        page_body = dedent("""
        # My Header
        
        My content
        """)
        page = Page.new(
            title="Page Title",
            url="http://example.com",
            body=page_body
        )

        mock_get_url(page)

        cli.command([str(self.default_url)], None, None, False)

        mock_stdout.assert_called_once_with(page_body)