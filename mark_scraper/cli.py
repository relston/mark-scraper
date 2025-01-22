import click
from . import scraper
from importlib.metadata import version, PackageNotFoundError

try:
    package_version = version("mark_scraper")
except PackageNotFoundError:
    package_version = "unknown"

@click.command()
@click.argument('url', type=click.STRING)
@click.option('--debug', '-d', is_flag=True, help='Open browser window and print network events during scrap')
@click.option('--silent', '-s', is_flag=True, help="Don't return the scraped content")
@click.version_option(version=package_version)
def command(url, debug, silent):
    """
    Markdown Scraper CLI

    Usage
    mark_scraper http://example.com
    """
    try:
        page = scraper.get(url, debug)
        if not silent:
            click.echo(page.body)
    except scraper.BrowserError:
        click.echo(f"BrowserError while fetching {url}", err=True)
        exit(1)
    except scraper.TimeoutError:
        click.echo(f"Timeout while fetching {url}", err=True)
        exit(1)