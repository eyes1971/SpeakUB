
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.10] - 2025-10-08

### Added
- **CFI Cache TTL Management**: Implemented Time-To-Live (TTL) mechanism in `CFIGenerator` with 5-minute expiration and automatic cleanup of expired cache entries to prevent memory leaks during long reading sessions
- **CFI Cache Size Limits**: Added configurable cache size limit (100 entries) with LRU-style cleanup when cache exceeds maximum size
- **TTS State Machine Error Recovery**: Enhanced TTS state machine in `EdgeTTSProvider` with complete error state transitions, allowing recovery from any state to ERROR and back to IDLE/STOPPED states
- **ThreadPoolExecutor Timeout Protection**: Added timeout handling in `PlaybackManager.stop_playback()` with 2-second timeout per future to prevent blocking during network failures
- **Specific Exception Handling**: Introduced granular exception handling in main application by importing and using specific exception classes (`ConfigurationError`, `TTSError`, `ParseError`) instead of broad `Exception` catching

### Changed
- **CFI Cache Structure**: Modified `CFIGenerator._indexed_cache` from `Dict[int, List[Any]]` to `Dict[int, Tuple[List[Any], float]]` to include timestamp for TTL tracking
- **TTS State Transitions**: Updated `valid_transitions` dictionary in `EdgeTTSProvider` to include ERROR state paths for all existing states
- **Exception Handling Strategy**: Replaced generic `except Exception` blocks with specific exception types in `EPUBReaderApp.__init__()` for better error categorization and debugging

### Technical Improvements
- **Memory Management**: Enhanced CFI caching system with automatic cleanup mechanisms to prevent unbounded memory growth
- **Error Recovery**: Improved TTS robustness by adding error state transitions, enabling graceful recovery from network or audio failures
- **Thread Safety**: Added timeout protection to thread pool operations, preventing UI freezing during TTS interruptions
- **Code Quality**: Refined exception handling throughout the application for better error traceability and maintenance
- **Performance Stability**: Implemented cache size limits and TTL expiration to maintain consistent performance during extended use

### Fixed
- **Memory Leak Prevention**: Resolved potential memory leaks in CFI caching by implementing TTL-based cache expiration and size limits
- **TTS State Machine Completeness**: Fixed incomplete state transitions in TTS provider by adding missing ERROR state paths
- **Thread Blocking Issues**: Prevented UI blocking during TTS stop operations by adding timeout handling to future completion waiting
- **Error Handling Precision**: Improved error handling specificity to prevent silent failures and enable better debugging

## [1.1.9] - 2025-10-07

### Added
- **Adaptive Cache System**: Implemented `AdaptiveCache` class with TTL (Time-To-Live) and LRU eviction for intelligent memory management in `ContentRenderer`
- **Performance Monitoring**: Added `PerformanceMonitor` class providing comprehensive system performance tracking, including cache hit rates, memory usage, and TTS state monitoring
- **Performance Benchmarks**: Created `test_performance_benchmarks.py` with comprehensive performance testing suite for cache operations, memory usage, and rendering performance
- **Cache Statistics API**: Added `get_cache_stats()` method to `ContentRenderer` for real-time cache performance monitoring

### Changed
- **Memory Management**: Replaced `OrderedDict`-based LRU cache in `ContentRenderer` with `AdaptiveCache` providing TTL expiration and performance statistics
- **Code Comments**: Converted remaining Chinese comments to English for better international accessibility and consistency
- **Project Cleanup**: Removed redundant `speakub/ui/ui_components.py` file containing duplicate `PanelTitle` class that was unused in favor of `speakub/ui/panel_titles.py`
- **TTS Responsiveness**: Improved TTS startup responsiveness by implementing a segmented timeout mechanism, allowing long-running synthesis operations to be interrupted by the user.
- **CFI Performance**: Optimized CFI (Canonical Fragment Identifier) generation by caching indexed node results, significantly improving performance during progress saving and location tracking.
- **Configuration Loading**: Enhanced configuration loading in the main application by integrating `ConfigManager`, improving robustness and adding logging for silent failures.
- **TTS State Machine**: Refactored `EdgeTTSProvider` to use the unified `TTSState` enum, eliminating the redundant `AudioState` and simplifying the state machine logic.
- **Development Tools Removal**: Removed `tools/` directory containing development and debugging scripts (`check_voices.py`, `debug_voices.py`, `simple_layout_check.py`, `simple_test.py`, `test_my_help_screen.py`, `voice_selector_demo.py`) to streamline project structure and reduce maintenance overhead

### Technical Improvements
- **Cache Performance**: Implemented TTL-based cache expiration (5 minutes) to prevent memory leaks from stale cached renderers
- **Memory Efficiency**: Added hardware-aware cache sizing that automatically adjusts cache size based on system memory (5-20 renderers)
- **Performance Monitoring**: Established comprehensive performance tracking with configurable monitoring intervals and historical data retention
- **Codebase Simplification**: Eliminated duplicate UI components and development-only tools, resulting in cleaner project structure and reduced complexity
- **Maintenance Reduction**: Removed non-production development scripts that were not part of the core application functionality
- **Error Handling**: Enhanced error handling in cache operations with proper logging and graceful degradation

### Performance Enhancements
- **Cache Hit Rate Optimization**: TTL mechanism ensures cache freshness while maintaining high hit rates
- **Memory Usage Control**: Adaptive sizing prevents excessive memory consumption on low-end hardware
- **System Monitoring**: Real-time performance metrics enable proactive optimization and troubleshooting
- **Benchmarking Framework**: Automated performance testing ensures consistent performance across releases

## [1.1.8] - 2025-10-06

### Fixed
- **AppInterface Protocol Assertion**: Fixed production environment crash by replacing `assert` statement with explicit `ValueError` exception in `TTSIntegration.__init__()`, ensuring proper error handling when app object doesn't conform to protocol.
- **EPUB Cache Strategy**: Fixed cache key normalization in `EPUBParser._read_chapter_from_zip()` by using `normalize_zip_path()` instead of raw zip paths, preventing cache misses on equivalent file paths and improving performance.
- **Test Suite Failures**: Fixed TTS integration tests by updating `MockApp` class to properly implement `AppInterface` protocol with required `bell()` and `query_one()` methods.
- **Network Recovery Configuration**: Replaced hardcoded network recovery parameters (30-minute timeout, 10-second intervals, Google DNS) with configurable values in `config.json`, allowing users to customize network behavior for different environments.

### Added
- **Custom Exception Classes**: Added `SpeakUBError`, `NetworkError`, `TTSError`, `ParseError`, `ConfigurationError`, `FileSizeError`, and `SecurityError` exception classes in `core/__init__.py` for better error categorization and handling.
- **Security Enhancements**: Added file size limits (500MB max) and zip bomb protection in `EPUBParser` to prevent malicious EPUB files from causing resource exhaustion.
- **Adaptive Memory Management**: Implemented hardware-aware cache sizing in `ContentRenderer` that automatically adjusts cache size based on system memory (5-20 renderers depending on RAM).
- **Hierarchical Configuration System**: Implemented `ConfigManager` class with hierarchical override system supporting defaults, config files, environment variables, and runtime overrides for flexible configuration management.
- **Performance Monitoring System**: Created `PerformanceMonitor` class providing comprehensive performance tracking, benchmarking, and system resource monitoring with configurable thresholds and slow operation detection.
- **Predictive Preloading System**: Implemented `PredictivePreloader` with reading pattern analysis and background chapter preloading to improve user experience by anticipating content needs.
- **Network Configuration System**: Added comprehensive network settings to configuration system including recovery timeout, check intervals, and connectivity test parameters.
- **Centralized Logging Configuration**: Created `utils/logging_config.py` module providing unified logging setup with file rotation, console output, and hierarchical logger naming.
- **Network Configuration API**: Added `get_network_config()` function to retrieve network settings from configuration file with proper defaults.

### Changed
- **Error Handling Classification**: Updated TTS engine error handling to raise specific `TTSError` exceptions instead of generic exceptions, improving error traceability and allowing callers to handle different error types appropriately.
- **Network Recovery Logic**: Modified `NetworkManager.monitor_network_recovery()` to use configuration values instead of hardcoded parameters, making network recovery behavior customizable.
- **Test Organization**: Replaced invalid test methods in `test_epub_parser.py` with proper cache functionality tests, ensuring test suite reliability.

### Technical Improvements
- **Configuration Management**: Enhanced configuration system with network-specific settings and validation, providing better user customization options.
- **Error Handling Precision**: Improved error handling throughout TTS subsystem by using specific exception types instead of broad `except Exception` blocks.
- **Thread Management**: Enhanced `PlaybackManager.shutdown()` with timeout protection and graceful degradation, preventing resource leaks during application termination.
- **Logging Infrastructure**: Established centralized logging configuration for better debugging and monitoring capabilities.
- **Test Reliability**: Fixed test suite issues that were preventing proper validation of core functionality.

## [1.1.8] - 2025-10-06

### Fixed
- **Terminal Auto-Close**: Fixed issue where terminal emulator would remain open after SpeakUB exits when launched from desktop environments. Modified `relaunch_in_terminal()` function to remove hold flags (`-H`, `-hold`) and add `; exit` to command strings, ensuring terminals close automatically after program completion.
- **TTS Pause/Resume Bug**: Fixed critical issue where pausing TTS playback would incorrectly create new temporary audio files instead of reusing existing ones. The `PlaybackManager.stop_playback()` method now correctly distinguishes between pause and stop operations, calling `tts_engine.pause()` for pause and `tts_engine.stop()` for stop. This prevents unnecessary TTS API calls and improves performance.
- **Memory Management (`PlaybackManager`)**: Fixed potential memory leak by adding periodic cleanup of completed futures in long TTS sessions, preventing unbounded accumulation of Future objects.
- **Memory Management (`ContentRenderer`)**: Increased renderer cache size from 5 to 20 to better handle frequent terminal resizing, preventing cache thrashing and improving performance.
- **Silent Error Handling**: Replaced all `except Exception: pass` statements in UI utilities with proper logging, improving debuggability without changing runtime behavior.

### Technical Improvements
- **TTS Debug Information**: Added comprehensive debugging information to TTS components including current audio file display in UI, detailed logging of pause/resume operations, and status tracking for better troubleshooting of TTS issues.
- **Performance (`EPUBParser`)**: Increased chapter cache size from 10 to 50 to improve navigation performance in large EPUB files with many chapters.
- **Performance (`Configuration`)**: Added file modification time-based caching to `get_tts_config()` to avoid redundant disk I/O during TTS operations.
- **Performance (`Hardware Detection`)**: Made hardware profile detection fully lazy-loaded to improve application startup time by deferring detection until first needed.
- **Code Quality**: Enhanced error messages in UI utilities with descriptive context for better troubleshooting.
- **Architecture (`PlaybackManager`)**: Improved code clarity by making `PlaylistManager` reference direct in `PlaybackManager.__init__()`, cleaned up unused imports, and fixed code formatting issues.

## [1.1.7] - 2025-10-06

### Fixed
- **Memory Leak (`PlaybackManager`)**: Fixed a memory leak in `PlaybackManager` by periodically cleaning completed `Future` objects during playback, preventing unbounded list growth in long sessions.
- **Memory Leak (`ContentRenderer`)**: Prevented a memory leak in `ContentRenderer` by implementing an LRU cache for renderers, limiting cache size and avoiding indefinite growth when the terminal is resized frequently.
- **Race Condition (`NetworkManager`)**: Resolved a race condition in `NetworkManager` by using a `threading.Lock` to protect access to shared flags, ensuring thread safety during network recovery monitoring.
- **Silent Failures (`TTSIntegration`)**: Improved error handling in `TTSIntegration.cleanup()` by replacing broad exception catches with more specific logging, preventing silent failures and potential resource leaks during shutdown.
- **Error Handling Precision**: Refined exception handling across the codebase (e.g., in `EPUBParser`) by catching specific errors instead of using broad `except Exception` blocks, making debugging more effective and preventing the suppression of unexpected issues.

### Technical Improvements
- **Performance (`EPUBParser`)**: Significantly improved chapter navigation and TTS playlist generation performance by adding an LRU cache to `EPUBParser.read_chapter()`, avoiding redundant file I/O from the EPUB zip.
- **Performance (`config.py`)**: Optimized application startup time by making hardware profile detection in `config.py` lazy. It now only runs once when first needed, rather than on every module import.
- **Performance (`get_tts_config`)**: Improved performance of configuration access by caching the TTS config in memory, eliminating redundant file I/O on every call to `get_tts_config()`.
- **Architecture (`TTS Module`)**: Reduced coupling and improved testability in the TTS module by resolving a circular dependency between `PlaylistManager` and `PlaybackManager`. `PlaybackManager` now receives a direct reference to `PlaylistManager`.
- **Code Quality (`ChapterManager`)**: Refactored the complex `_build_chapters_from_spine_and_toc` method in `ChapterManager` into smaller, single-responsibility helper methods, improving readability and making it easier to unit test.
- **Code Readability**: Replaced magic numbers (e.g., `180` in `NetworkManager`) with descriptive named constants to improve code clarity and maintainability.
- **Robustness**: Standardized `None` checks to use explicit `is not None` comparisons, preventing potential bugs where values like `0` could be misinterpreted as `False`.

### Testing
- **CFI Module Coverage**: Added a new test suite for the `CFI` (Canonical Fragment Identifier) module to ensure the robustness of progress tracking and location saving/restoring logic.
- **TTS Integration Tests**: Introduced integration tests for the TTS state machine to validate transitions between PLAYING, PAUSED, and STOPPED states, including network error recovery paths.

## [1.1.6] - 2025-10-04

### Added
- **Event-Driven Audio Playback Monitoring**: Implemented `pygame.mixer.music.set_endevent()` for more efficient audio playback waiting, reducing CPU usage by 50-90% during TTS playback
- **LRU Cache Optimization**: Added `functools.lru_cache` decorator to content renderer for better performance with repeated content rendering

### Changed
- **TTS Worker Management**: Replaced on-demand thread creation for TTS playback with a `ThreadPoolExecutor` to improve performance and resource management.
- **TTS Module Architecture Refactoring**: Major restructuring of TTS integration module for improved maintainability and separation of concerns
  - Created `PlaylistManager` class to handle playlist generation, indexing, and chapter loading operations
  - Created `PlaybackManager` class to manage TTS playback thread lifecycle (start, pause, stop)
  - **Performance**: Optimized logging in performance-critical EPUB parsing paths (`toc_parser.py`, `epub_parser.py`) by using conditional `logger.debug` calls. This reduces CPU overhead when debug logging is disabled.
  - Refactored `TTSIntegration` as coordinator with backward compatibility layer
  - Improved code organization with single responsibility principle implementation
- **Tools Documentation**: Translated `tools/README.md` from Chinese to English for better international accessibility
- **Test File Paths**: Replaced hardcoded Chinese paths in test files with English placeholders for cross-platform compatibility
- **Network Error Recovery**: The network recovery monitor (`monitor_network_recovery`) now has a 30-minute timeout instead of polling indefinitely. This prevents the background thread from getting stuck and improves resource management. A notification is shown to the user upon timeout.

### Fixed
- **Logging Verbosity**: Adjusted the TTS manager's shutdown message log level from `INFO` to `DEBUG`.
- **TTS Worker Parameter Passing**: Fixed `find_and_play_next_chapter_worker` function parameter passing issue that caused TypeError when TTS playlist was empty
- **Code Comments**: Reviewed and maintained appropriate Chinese content in functional comments and configuration examples
- **TTS Playback Memory Leak**: Prevented a potential memory leak in `PlaybackManager` by ensuring the list of `Future` objects from the thread pool is regularly cleaned of completed tasks. This prevents the list from growing indefinitely during long-running sessions.
- **NCX Table of Contents Hierarchical Parsing**: Fixed EPUB2 NCX parsing to properly handle nested navPoint structures instead of flattening all entries. Now correctly displays collapsible multi-level directories in the UI for books with complex chapter hierarchies.
- **Cache Management**: Fixed a potential memory leak and instability issue in `ContentRenderer` by replacing the global `@lru_cache` with an instance-level cache. This ensures that renderer instances are properly isolated and garbage collected, improving stability in multi-instance scenarios.
- **Silent Failures**: Added proper logging to `try/except: pass` blocks across the application (e.g., in `ProgressManager`) to prevent errors from being silently ignored. This improves debuggability without changing runtime behavior.
- **CFI Resolution Fallback**: Added warning logs when EPUB Canonical Fragment Identifier (CFI) resolution fails and the system falls back to less precise line numbers, making progress-loading issues easier to diagnose.

### Technical Improvements
- **State Management Refactoring**: Improved separation of concerns by decoupling `ProgressManager` from `EPUBReaderApp`. The polling callback is now passed via dependency injection, making the state management logic more modular and maintainable.
- **Facade Pattern Refinement**: Strengthened the Facade pattern by adding a high-level `get_next_chapter_content_lines` method to `EPUBManager`. This decouples the TTS module from the internal implementation details of chapter loading and rendering, improving modularity and maintainability.
- **TTS Playlist State Refactoring**: Resolved a circular dependency between `TTSIntegration` and `PlaylistManager` by making `PlaylistManager` the sole owner of the playlist state. This simplifies the architecture, improves testability, and clarifies data flow within the TTS module.
- **TTS Architecture**: Enhanced modularity with dedicated managers for playlist and playback operations
- **Code Maintainability**: Improved separation of concerns and reduced complexity in TTS integration
- **Backward Compatibility**: Maintained all existing APIs while improving internal structure
- **Code Readability**: Replaced magic numbers (e.g., `180`) with descriptive named constants to improve code clarity and maintainability.
- **Robustness**: Standardized `None` checks to use explicit `is not None` comparisons, preventing potential bugs where values like `0` could be misinterpreted.
- **Error Handling Precision**: Refined exception handling by catching specific errors instead of using broad `except Exception` blocks, making debugging more effective and preventing the suppression of unexpected issues.
- **Audio Player Architecture**: Enhanced `play_and_wait()` method with event-driven monitoring and fallback polling mechanism
- **Cache Management**: Improved renderer caching with automatic LRU eviction and size limits
- **Error Handling**: Added robust error handling for pygame event system initialization
- **Error Handling**: Enhanced overall application stability by replacing silent error suppression with explicit logging.
- **Progress Migration**: Added logging to track the migration of old, line-number-based progress files to the new CFI-based format, improving maintainability.
- **Code Quality**: Maintained functional Chinese content in pronunciation correction examples and text processing comments
- **Protocol Compliance Enforcement**: Refactored `EPUBReaderApp` to correctly implement the `AppInterface` protocol using properties (`@property`) instead of direct attribute access. This ensures type safety and interface consistency between components.
- **Runtime Interface Validation**: Added runtime checking for `AppInterface` using the `@runtime_checkable` decorator and `isinstance()` validation. This prevents subtle bugs by ensuring the application object strictly conforms to the protocol expected by modules like `TTSIntegration`, making the architecture more robust.

## [1.1.5] - 2025-10-04

### Changed
- **Project Structure Refactoring**: Reorganized TTS module structure for better maintainability
- **Directory Consolidation**: Merged `tts_integration` directory into `tts/ui` subdirectory
- **Import Path Updates**: Updated all import statements to reflect new module organization

### Technical Improvements
- **Code Organization**: Consolidated TTS-related functionality under unified `speakub.tts` module
- **Import Cycle Resolution**: Fixed circular import issues between TTS modules
- **Module Structure**: Improved separation between core TTS functionality and UI integration
- **File Cleanup**: Removed empty and unused files and directories to streamline codebase

### Fixed
- **TTS Import Issues**: Resolved TTS functionality availability detection and import problems
- **Module Dependencies**: Fixed circular dependencies in TTS integration components

## [1.1.4] - 2025-10-02

### Fixed
- **EPUB2 NCX Table of Contents Title Mapping**: Fixed critical issue where chapter titles became "Untitled Chapter" after page navigation when EPUB files used NCX (toc.ncx) format. The parser was correctly displaying TOC hierarchy in the UI but failing to populate the raw_chapters list needed for chapter title mapping in the chapter manager.

### Technical Improvements
- Added `_flatten_toc_nodes_for_raw_list()` helper function to recursively flatten hierarchical TOC nodes into a flat chapter list
- Enhanced EPUB parser to ensure raw_chapters is populated for both nav.xhtml and toc.ncx parsing paths
- Fixed data flow gap between EPUBParser and ChapterManager for NCX-based EPUB files
- Improved chapter title inheritance logic to work consistently across all EPUB formats

## [1.1.3] - 2025-10-01

### Added
- **Automatic Desktop Integration**: Desktop entry is automatically created on first run, enabling right-click "Open with SpeakUB" and double-click EPUB file opening
- Desktop entry uses direct `speakub %f` command with automatic terminal detection
- Desktop installation occurs in `main()` function to work with setuptools entry points

### Changed
- **Desktop Entry Generation**: Simplified `.desktop` file creation to leverage existing terminal detection logic instead of hardcoding terminal commands
- **Installation Logic**: Moved desktop installation from `if __name__ == "__main__"` to `main()` function for compatibility with pip-installed scripts
- **Parameter Handling**: Fixed argument passing to properly handle filenames with special characters (spaces, brackets, etc.) when launched from desktop environments like rofi
- **Desktop Exec Command**: Updated `.desktop` file to use quoted parameters `Exec=speakub "%f"` for better shell compatibility

### Fixed
- **Desktop Launch Issues**: Modified application to always relaunch in a terminal emulator, ensuring consistent behavior when launched from rofi, file managers, or other desktop environments
- **Special Character Handling**: Resolved issues with filenames containing spaces, brackets, and other special characters when launched from desktop environments

### Fixed
- **Special Character Handling**: Resolved issues with launching SpeakUB from rofi or other desktop environments when EPUB filenames contain spaces, brackets, or other special characters

## [1.1.2] - 2025-10-01

### Added
- **Automatic Terminal Detection**: Added logic to automatically detect if the application is running in a terminal environment. If not (e.g., launched from file manager), it will automatically relaunch in a terminal emulator.
- **System Default Terminal Support**: The terminal detection now prioritizes the system's default terminal (via `$TERMINAL` environment variable) before falling back to a list of common terminal emulators.
- **Terminal Emulator Detection**: Supports detection and launching in popular terminal emulators including Alacritty, Kitty, WezTerm, GNOME Terminal, XFCE4 Terminal, Konsole, XTerm, URXVT, and ST.

### Changed
- **CLI Comments**: Translated all Chinese comments in `cli.py` to English for better international accessibility.

### Technical Improvements
- Enhanced CLI entry point with robust terminal environment checking
- Improved error handling for terminal emulator detection and launching
- Added desktop notifications as fallback when terminal emulator is not found

## [1.1.1] - 2025-09-30

### Fixed
- **EPUB Table of Contents Hierarchical Parsing**: Fixed TOC parsing to properly handle nested structures in EPUB files. When nav.xhtml contains only flat chapter lists, the parser now automatically falls back to toc.ncx for better hierarchical organization. This resolves issues where books with complex chapter hierarchies (like multi-part novels) were displayed as flat lists instead of collapsible nested directories.

### Technical Improvements
- Enhanced EPUB parser with intelligent fallback logic between nav.xhtml and toc.ncx
- Improved XML structure detection for malformed EPUB files
- Better handling of EPUB2/EPUB3 TOC format differences
- Added debug logging for TOC source selection

## [1.1.0] - 2025-09-06

### Added
- **Chinese Pronunciation Corrections**: New optional feature for customizing Chinese character pronunciation in TTS
- Automatic creation of corrections configuration file with instructions and examples
- Smart filtering of instruction keys (starting with `_`) in corrections file
- Enhanced content widget with improved text processing and English word break handling
- Comprehensive documentation for pronunciation corrections feature

### Changed
- Updated content widget `get_paragraph_text` method with better text concatenation logic
- Improved error handling for pronunciation corrections loading
- Enhanced build system with updated version management

### Fixed
- Fixed Flake8 linting issues in content widget
- Resolved line length violations in code comments
- Improved code formatting and style consistency

### Technical Improvements
- Added `load_pronunciation_corrections()` and `save_pronunciation_corrections()` functions to config module
- Implemented automatic corrections file generation with user-friendly instructions
- Enhanced text processing with regex-based word boundary detection
- Updated build configuration for better package management

### Documentation
- Added detailed Chinese pronunciation corrections usage guide to README
- Included corrections.json file format specification
- Added version history section with changelog
- Updated feature list to include pronunciation corrections

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
- **1.1.6**: Major refactoring for TTS architecture, performance optimization, and error handling improvements.
- **1.1.5**: Project structure refactoring and TTS module reorganization
- **1.1.4**: Fixed EPUB2 NCX table of contents title mapping issue
- **1.1.3**: Added automatic desktop integration and improved desktop launching
- **1.1.2**: Added automatic terminal detection and CLI improvements
- **1.1.1**: Fixed EPUB table of contents hierarchical parsing
- **1.1.0**: Added Chinese pronunciation corrections feature
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
