










# Contributing to SpeakUB

Thank you for your interest in contributing to SpeakUB! This document provides guidelines and information for contributors.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Reporting Issues](#reporting-issues)
- [Documentation](#documentation)

## Code of Conduct

This project follows a code of conduct to ensure a welcoming environment for all contributors. By participating, you agree to:

- Be respectful and inclusive
- Focus on constructive feedback
- Accept responsibility for mistakes
- Show empathy towards other contributors
- Help create a positive community

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Terminal with Unicode support

### Quick Start

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/eyes1971/SpeakUB.git
   cd SpeakUB
   ```
3. Set up the development environment (see below)
4. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Setup

### 1. Install Dependencies

```bash
# Install core dependencies
pip install -e .

# Install development dependencies
pip install -e .[dev]

# Install TTS dependencies (optional)
pip install -e .[tts]

# Install all dependencies
pip install -e .[all]
```

### 2. Install Pre-commit Hooks

```bash
pre-commit install
```

This will automatically run code quality checks before each commit.

### 3. Verify Setup

```bash
# Run tests
pytest

# Check code formatting
black --check speakub/
isort --check-only speakub/

# Type checking
mypy speakub/

# Linting
flake8 speakub/
```

## Development Workflow

### 1. Choose an Issue

- Check the [Issues](https://github.com/eyes1971/SpeakUB/issues) page
- Look for issues labeled `good first issue` or `help wanted`
- Comment on the issue to indicate you're working on it

### 2. Create a Branch

```bash
git checkout -b feature/issue-number-description
# or
git checkout -b fix/issue-number-description
# or
git checkout -b docs/issue-number-description
```

### 3. Make Changes

- Write clear, focused commits
- Test your changes thoroughly
- Update documentation if needed
- Follow the coding standards below

### 4. Test Your Changes

```bash
# Run the full test suite
pytest

# Run specific tests
pytest tests/test_specific_feature.py

# Run with coverage
pytest --cov=speakub --cov-report=html

# Run type checking
mypy speakub/
```

### 5. Update Documentation

- Update README.md if adding new features
- Update docstrings for new functions/classes
- Add examples for new functionality
- Update CHANGELOG.md for user-facing changes

## Coding Standards

### Python Style

This project follows PEP 8 with some modifications:

- **Line Length**: 88 characters (Black default)
- **Imports**: Sorted with isort
- **Formatting**: Enforced with Black
- **Type Hints**: Required for new code, encouraged for existing code

### Code Quality Tools

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking

### Pre-commit Hooks

The following checks run automatically on commit:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.7.0
    hooks:
      - id: black
        language_version: python3

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: ["--profile", "black"]

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.5.1
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
```

### Commit Messages

Follow conventional commit format:

```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Testing
- `chore`: Maintenance

Examples:
```
feat: add voice selection panel
fix: resolve TTS initialization error
docs: update installation instructions
```

## Testing

### Test Structure

```
tests/
├── test_epub_parser.py      # EPUB parsing tests
├── test_content_renderer.py # Content rendering tests
├── test_tts_integration.py  # TTS integration tests
├── test_ui_components.py    # UI component tests
└── test_cpu_optimization.py # Performance tests
```

### Writing Tests

- Use descriptive test names
- Test both positive and negative cases
- Mock external dependencies
- Include docstrings for complex tests

Example:
```python
def test_voice_selection():
    """Test voice selection functionality."""
    # Arrange
    voice_selector = VoiceSelector()
    voice = "en-US-AriaRUS"

    # Act
    voice_selector.select_voice(voice)

    # Assert
    assert voice_selector.current_voice == voice
```

### Running Tests

```bash
# All tests
pytest

# Specific test file
pytest tests/test_tts_integration.py

# Specific test
pytest tests/test_tts_integration.py::TestTTSIntegration::test_initialization

# With coverage
pytest --cov=speakub --cov-report=html

# Verbose output
pytest -v

# Stop on first failure
pytest -x
```

## Submitting Changes

### Pull Request Process

1. **Update your branch**:
   ```bash
   git checkout main
   git pull origin main
   git checkout your-branch
   git rebase main
   ```

2. **Ensure tests pass**:
   ```bash
   pytest
   mypy speakub/
   black --check speakub/
   isort --check-only speakub/
   ```

3. **Create a Pull Request**:
   - Use a descriptive title
   - Fill out the PR template
   - Reference related issues
   - Add screenshots for UI changes

4. **PR Template**:
   ```markdown
   ## Description
   Brief description of changes

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Breaking change
   - [ ] Documentation update

   ## Testing
   - [ ] Tests added/updated
   - [ ] Manual testing performed
   - [ ] All tests pass

   ## Screenshots (if applicable)
   Add screenshots for UI changes

   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Documentation updated
   - [ ] Tests pass
   - [ ] Ready for review
   ```

### Code Review Process

- At least one maintainer review required
- Address review comments
- CI checks must pass
- Squash commits if requested
- Maintainers will merge approved PRs

## Reporting Issues

### Bug Reports

When reporting bugs, please include:

1. **Clear title** describing the issue
2. **Steps to reproduce**:
   ```bash
   # Commands or steps that reproduce the issue
   speakub example.epub
   # Then press Ctrl+C
   ```
3. **Expected behavior**
4. **Actual behavior**
5. **Environment**:
   - OS: Ubuntu 22.04
   - Python: 3.10.6
   - SpeakUB version: 1.0.0
6. **Logs or error messages**
7. **Screenshots** (if applicable)

### Feature Requests

For feature requests, please include:

1. **Clear description** of the proposed feature
2. **Use case** - why is this feature needed?
3. **Proposed implementation** (optional)
4. **Alternatives considered** (optional)

## Documentation

### Updating Documentation

- Keep README.md up to date
- Add docstrings to all public functions/classes
- Update CHANGELOG.md for user-facing changes
- Add examples for new features

### Documentation Standards

```python
def process_epub(file_path: str) -> dict:
    """
    Process an EPUB file and extract its contents.

    Args:
        file_path: Path to the EPUB file

    Returns:
        Dictionary containing extracted data

    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If the file is not a valid EPUB

    Example:
        >>> data = process_epub("book.epub")
        >>> print(data.keys())
        dict_keys(['title', 'chapters', 'metadata'])
    """
```

## Getting Help

- **Issues**: [GitHub Issues](https://github.com/eyes1971/SpeakUB/issues)
- **Discussions**: [GitHub Discussions](https://github.com/eyes1971/SpeakUB/discussions)
- **Documentation**: [Read the Docs](https://speakub.readthedocs.io/)

## Recognition

Contributors will be recognized in:
- CHANGELOG.md for significant contributions
- GitHub's contributor insights
- Project documentation

Thank you for contributing to SpeakUB! 🎉
