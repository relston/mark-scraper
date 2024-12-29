# Mark Scraper
CLI to scrape webpages and return them in markdown format

```bash
mark-scraper http://example.com
# # Example
# This is an example website
```

# TODO
- Also save html
    - `mark-scraper -h/--html example.com.html http://example.com > example.com.md`
- Take a screen shot of web page
    - `mark-scraper -s/--screenshot screenshot.png http://example.com > example.com.md`
- Add Page Caching
    - Will return from cache if exists `mark-scraper -c/--cache http://example.com > example.com.md`
    - Bust cache `mark-scraper -b/--bust-cache http://example.com > example.com.md`
    - Clear cache `rm -rf .mark-scraper/cache`
- Add log of pages scrapped

# Development
```bash
uv sync
uv run pytest
```

https://packaging.python.org/en/latest/guides/writing-pyproject-toml/