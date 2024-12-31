import click
from . import scraper
from importlib.metadata import version, PackageNotFoundError

try:
    package_version = version("mark_scraper")
except PackageNotFoundError:
    package_version = "unknown"

@click.command()
@click.argument('url', type=click.STRING)
@click.version_option(version=package_version)
def command(url):
    """
    Markdown Scraper CLI

    Usage
    mark_scraper http://example.com
    """
    try:
        page = scraper.get(url)
        click.echo(page.body)
    except scraper.BrowserError:
        click.echo(f"BrowserError while fetching {url}", err=True)
        exit(1)
    except scraper.TimeoutError:
        click.echo(f"Timeout while fetching {url}", err=True)
        exit(1)