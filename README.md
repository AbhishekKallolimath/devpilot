# DevPilot

DevPilot is a Python-based CLI tool that helps developers audit projects, verify development environments, and detect potential security issues.

## Features

- System Doctor
- Project Audit
- Secret Scanner
- Project Health Score

## Installation

```bash
pip install -r requirements.txt
```
## Usage

```bash
python -m app.main doctor
python -m app.main audit
python -m app.main scan
```

## Roadmap

- Secret detection with regex
- HTML reports
- JSON exports
- Docker analysis
- GitHub Actions analysis

## Tech Stack

- Python
- Typer
- Rich
- Git

## Current Features

- ✅ System health checks
- ✅ Git repository validation
- ✅ Project structure auditing
- ✅ Secret and `.env` file scanning
- ✅ Project statistics
- ✅ Project health scoring
- ✅ Automated tests with Pytest
- ✅ GitHub Actions CI

## CLI Commands

```bash
python -m app.main doctor
python -m app.main audit
python -m app.main scan
python -m app.main stats
python -m app.main health
python -m app.main version






----
---