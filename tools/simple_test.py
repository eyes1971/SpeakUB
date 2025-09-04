
#!/usr/bin/env python3
"""
Simple test for EdgeTTSProvider
"""

import asyncio

try:
    from speakub.tts.edge_tts_provider import EdgeTTSProvider
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("❌ Unable to import EdgeTTSProvider")
    exit(1)


async def test_provider():
    """Test provider"""
    print("🔄 Creating EdgeTTSProvider...")

    try:
        provider = EdgeTTSProvider()
        print("✅ EdgeTTSProvider created successfully")

        print("🔄 Fetching available voices...")
        # Clear cache to force re-fetch
        provider._voices_cache = None
        voices = await provider.get_available_voices()
        print(f"✅ Retrieved {len(voices)} voices")

        if voices:
            print("\nFirst 3 voices:")
            for i, voice in enumerate(voices[:3]):
                print(
                    f"• {voice.get('name', 'Unknown')} ({voice.get('short_name', '')})")
                print(
                    f"  Gender: {voice.get('gender', '')}, Locale: {voice.get('locale', '')}")

        # Test voice settings
        current_voice = provider.get_current_voice()
        print(f"\nCurrent voice: {current_voice}")

        # Test setting voice
        test_voice = "zh-CN-XiaoxiaoNeural"
        if provider.set_voice(test_voice):
            print(f"✅ Successfully set voice to: {test_voice}")
            print(f"Current voice: {provider.get_current_voice()}")
        else:
            print(f"❌ Failed to set voice: {test_voice}")

    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_provider())

