
#!/usr/bin/env python3
"""
Debug voice data structure
"""

import asyncio

try:
    import edge_tts
    from speakub.tts.edge_tts_provider import EdgeTTSProvider
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("❌ edge-tts not installed")
    exit(1)


async def debug_voices():
    """Debug voice data"""
    print("🔄 Fetching voice data...")

    try:
        # Use edge_tts directly
        voices = await edge_tts.list_voices()
        print(f"✅ Retrieved {len(voices)} voices from edge_tts")

        # Check structure of first 3 voices
        for i, voice in enumerate(voices[:3]):
            print(f"\n--- Voice {i+1} ---")
            for key, value in voice.items():
                print(f"{key}: {value}")

        # Use EdgeTTSProvider
        print("\n" + "="*50)
        print("🔄 Using EdgeTTSProvider...")
        provider = EdgeTTSProvider()
        provider_voices = await provider.get_available_voices()
        print(
            f"✅ Retrieved {len(provider_voices)} voices from EdgeTTSProvider")

        # Check structure of first 3 voices
        for i, voice in enumerate(provider_voices[:3]):
            print(f"\n--- Provider Voice {i+1} ---")
            for key, value in voice.items():
                print(f"{key}: {value}")

        # Find Chinese voices
        chinese_voices = []
        female_voices = []
        female_chinese_voices = []

        for voice in provider_voices:
            locale = voice.get('locale', '')
            gender = voice.get('gender', '')

            if locale.startswith(('zh-CN', 'zh-TW')):
                chinese_voices.append(voice)

            if gender.lower() == 'female':
                female_voices.append(voice)

            if (gender.lower() == 'female' and
                    locale.startswith(('zh-CN', 'zh-TW'))):
                female_chinese_voices.append(voice)

        print("\nStatistics:")
        print(f"Chinese voices: {len(chinese_voices)}")
        print(f"Female voices: {len(female_voices)}")
        print(f"Female Chinese voices: {len(female_chinese_voices)}")

        if female_chinese_voices:
            print("\nFemale Chinese voices:")
            for voice in female_chinese_voices:
                print(
                    f"• {voice.get('short_name', '')} - {voice.get('locale', '')} - {voice.get('gender', '')}")

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(debug_voices())

