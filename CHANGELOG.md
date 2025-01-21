# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.1] - 2025-01-20
### Fixed
- No longer hanging trying to get content from emptry frames
### Changed
- Browser is now in headless mode

## [0.2.0] - 2025-01-20
### Changed
- Replaced pyppeteer with playwright as a backend

## [0.1.3] - 2025-01-20
### Changed
- Scraper now waits to [networkidle2](https://pyppeteer.github.io/pyppeteer/_modules/pyppeteer/page.html#Page.goto) before returning

## [0.1.2] - 2025-01-07
### Removed
- `ipython` reference in the main scraper file

## [0.1.1] - 2025-01-07
### Added
- `BrowserError` and `TimeoutError` as public exceptions
- `ipython` dev dependency
### Fixed
- CLI now longer print stack traces for `BrowserError` and `TimeoutError`
- Scraper no longer errors on blank html tags

## [0.1.0] - 2024-12-28
### Added
- CHANGELOG.md