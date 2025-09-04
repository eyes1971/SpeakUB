
#!/usr/bin/env python3
"""
Check available voices for edge-tts
"""

import asyncio

try:
    import edge_tts
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("❌ edge-tts not installed")
    exit(1)


async def check_voices():
    """Check available voices"""
    print("🔄 Fetching available voice list...")

    try:
        voices = await edge_tts.list_voices()
        print(f"✅ Found {len(voices)} voices")

        # Count different types of voices
        chinese_voices = []
        female_voices = []
        female_chinese_voices = []

        for voice in voices:
            locale = voice.get('Locale', '')
            gender = voice.get('Gender', '')

            if locale.startswith(('zh-CN', 'zh-TW')):
                chinese_voices.append(voice)

            if gender.lower() == 'female':
                female_voices.append(voice)

            if (gender.lower() == 'female' and
                    locale.startswith(('zh-CN', 'zh-TW'))):
                female_chinese_voices.append(voice)

        print(f"Chinese voices: {len(chinese_voices)}")
        print(f"Female voices: {len(female_voices)}")
        print(f"Female Chinese voices: {len(female_chinese_voices)}")

        if female_chinese_voices:
            print("\n🎤 Female Chinese voice list:")
            print("-" * 60)
            for voice in female_chinese_voices:
                name = voice.get('Name', 'Unknown')
                short_name = voice.get('ShortName', '')
                local_name = voice.get('LocalName', '')
                locale = voice.get('Locale', '')
                print(f"• {local_name} ({short_name}) [{locale}]")
                print(f"  Full name: {name}")
        else:
            print("\n❌ No female Chinese voices found")

            # Show some available Chinese voices as reference
            if chinese_voices:
                print("\n📋 Available Chinese voices:")
                for voice in chinese_voices[:5]:  # Show only first 5
                    name = voice.get('Name', 'Unknown')
                    gender = voice.get('Gender', '')
                    print(f"• {name} (Gender: {gender})")

    except Exception as e:
        print(f"❌ Failed to fetch voice list: {e}")


if __name__ == "__main__":
    asyncio.run(check_voices())

