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


# Issue Check PYTHONPATH
Ensure that the directory containing your package is in the `PYTHONPATH`. This can be temporarily set in the terminal before running tests:
```bash
export PYTHONPATH=${PYTHONPATH}:/home/relston/projects/mark_scraper
```
Add a configuration in `pyproject.toml` for `pytest` to include the source directory:

```toml
[tool.pytest.ini_options]
pythonpath = ["."]
```

This will make `pytest` aware of modules in the current directory.


https://packaging.python.org/en/latest/guides/writing-pyproject-toml/