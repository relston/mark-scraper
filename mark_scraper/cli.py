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
    page = scraper.get(url)
    click.echo(page.body)