# Changelog

All notable changes to sinner will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-01-17

### Added

- Initial release of sinner v0.1
- Core CLI commands:
  - `name` - Generate professional names for code elements
  - `commit` - Create conventional commit messages
  - `comment` - Generate squash/merge comments from git history
  - `explain` - Explain code and technical concepts
  - `config` - Show current configuration
- Git integration for reading commit history
  - Support for `--count` flag to specify number of commits
  - Support for `--since` flag for date-based filtering
- Local-first architecture with LM Studio integration
- Explicit command routing (no LLM intent detection)
- Isolated, focused prompt templates
- ASCII banner on `--version`
- Comprehensive help text for all commands
- Clean, paste-ready output formatting

### Architecture

- Modular structure with `/core` and `/utils`
- Isolated LLM client for easy swapping
- Controller pattern for explicit command routing
- Typer-based CLI with rich help output
- Environment-based configuration via `.env`

### Documentation

- Comprehensive README with installation and usage
- Quick start guide (QUICKSTART.md)
- Example environment configuration (.env.example)
- Sanity test suite for core functionality

### Design Principles

- Local-only (no cloud, no accounts, no telemetry)
- Working > perfect
- Explicit routing, no magic
- Clean output, no noise
- Minimal dependencies

[0.1.0]: https://github.com/clasei/sinner/releases/tag/v0.1.0
