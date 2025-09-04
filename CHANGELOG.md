# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-08-20

### Added
- Initial release of SpeakUB - A rich terminal EPUB reader with TTS support
- Full EPUB 2 and EPUB 3 format support
- Text-to-Speech functionality using Microsoft Edge-TTS
- Beautiful terminal UI with Rich and Textual frameworks
- Smart navigation with hierarchical table of contents
- Progress tracking and automatic position saving
- Image display support (optional)
- Comprehensive keyboard shortcuts
- TTS controls with speed and volume adjustment
- Voice selection panel
- CPU optimization features for better performance
- Extensive configuration options
- Development tools and testing framework

### Features
- 🎨 Rich Terminal UI - Beautiful interface with Rich and Textual
- 📖 Full EPUB Support - Handles EPUB 2 and EPUB 3 formats
- 🔊 Text-to-Speech - Built-in TTS using Microsoft Edge-TTS
- 📑 Smart Navigation - Table of contents with hierarchical chapters
- 💾 Progress Tracking - Automatically saves your reading position
- 🎯 Seamless Reading - Navigate between chapters without interruption
- 🖼️ Image Support - View embedded images (optional)
- ⌨️ Keyboard Shortcuts - Efficient navigation with familiar keys
- 🎛️ TTS Controls - Play, Pause, Stop with speed/volume control

### Technical Improvements
- CPU optimization with idle mode detection
- Adaptive polling frequency for better performance
- Content rendering caching
- Background process management
- Comprehensive test suite with pytest
- Type checking with mypy
- Code formatting with black and isort
- Linting with flake8

### Dependencies
- Core: beautifulsoup4, wcwidth, html2text, rich, textual
- TTS: edge-tts, pygame
- Images: fabulous, Pillow
- Development: pytest, black, flake8, mypy, pre-commit

## [Unreleased]

### Planned
- Bug fixes and performance improvements
- Additional voice options
- Enhanced accessibility features
- Support for more EPUB features
- Improved error handling

---

## Development Notes

### Version History
- **1.0.0**: Initial stable release
- **0.x.x**: Development versions (internal)

### Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

### Acknowledgments
- Rich - For the beautiful terminal UI framework
- Textual - For the modern TUI components
- BeautifulSoup - For robust HTML parsing
- Edge-TTS - For high-quality text-to-speech
- html2text - For HTML to text conversion
