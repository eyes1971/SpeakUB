
#!/usr/bin/env python3
"""
Test if my_help_screen.py contains voice functionality
"""


def test_my_help_screen():
    """Test the content of my_help_screen.py"""
    print("🔍 Checking my_help_screen.py content...")

    with open('speakub/ui/my_help_screen.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # Check key features
    checks = [
        ("TTS_AVAILABLE", "TTS_AVAILABLE" in content),
        ("EdgeTTSProvider import",
         "from speakub.tts.edge_tts_provider import EdgeTTSProvider" in content),
        ("Voice selection area", "TTS voice selection area" in content),
        ("Test voice button", "Test voice" in content),
        ("Voice selection dropdown", "voice-select" in content),
        ("_initialize_tts method", "_initialize_tts" in content),
        ("_test_current_voice method", "_test_current_voice" in content),
        ("on_select_changed method", "on_select_changed" in content),
        ("on_button_pressed method", "on_button_pressed" in content),
    ]

    print("\n📋 Feature check results:")
    print("-" * 50)

    all_passed = True
    for check_name, passed in checks:
        status = "✅" if passed else "❌"
        print("25")
        if not passed:
            all_passed = False

    print("-" * 50)

    if all_passed:
        print("🎉 my_help_screen.py contains all voice features!")
    else:
        print("⚠️  my_help_screen.py is missing some voice features")

    # Display file size and line count
    lines = content.split('\n')
    print(f"\n📊 File statistics:")
    print(f"   Total lines: {len(lines)}")
    print(f"   File size: {len(content)} characters")

    # Display voice-related lines
    print(f"\n🎤 Voice-related content preview:")
    voice_lines = [i for i, line in enumerate(
        lines, 1) if 'TTS' in line or 'voice' in line.lower()]
    for line_num in voice_lines[:10]:  # Show only first 10
        print("4")

    if len(voice_lines) > 10:
        print(f"   ... and {len(voice_lines) - 10} more voice-related lines")


if __name__ == "__main__":
    test_my_help_screen()

