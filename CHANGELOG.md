# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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