
#!/usr/bin/env python3
"""
Standalone voice selector demo script
Demonstrates how to switch edge-tts Voice when running the script
"""

import asyncio
import sys
from typing import List, Dict, Any

try:
    import edge_tts
    from speakub.tts.edge_tts_provider import EdgeTTSProvider
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False


class VoiceSelectorDemo:
    """Voice selector demo class"""

    def __init__(self):
        self.tts_provider = None
        self.female_chinese_voices: List[Dict[str, Any]] = []
        self.current_voice = ""

    async def initialize(self) -> bool:
        """Initialize TTS provider"""
        if not TTS_AVAILABLE:
            print("❌ edge-tts not installed, please run: pip install edge-tts")
            return False

        try:
            print("🔄 Initializing TTS provider...")
            self.tts_provider = EdgeTTSProvider()

            print("🔄 Loading available voices...")
            voices = await self.tts_provider.get_available_voices()

            # Filter female Chinese voices
            self.female_chinese_voices = [
                voice for voice in voices
                if voice.get('gender', '').lower() == 'female' and
                voice.get('locale', '').startswith(('zh-CN', 'zh-TW'))
            ]

            if not self.female_chinese_voices:
                print("❌ No female Chinese voices found")
                return False

            # Set default voice
            self.current_voice = self.tts_provider.get_current_voice()
            print(
                f"✅ Initialization complete, found {len(self.female_chinese_voices)} female Chinese voices")
            return True

        except Exception as e:
            print(f"❌ Initialization failed: {e}")
            return False

    def display_voice_list(self) -> None:
        """Display voice list"""
        print("\n🎤 Available female Chinese voices:")
        print("-" * 60)
        for i, voice in enumerate(self.female_chinese_voices, 1):
            local_name = voice.get('local_name', voice.get(
                'display_name', voice.get('short_name', 'Unknown')))
            short_name = voice.get('short_name', '')
            locale = voice.get('locale', '')
            current_marker = " ← Current" if short_name == self.current_voice else ""
            print(
                f"{i:2d}. {local_name} ({short_name}) [{locale}]{current_marker}")
        print("-" * 60)

    def get_voice_choice(self) -> str:
        """Get user's voice choice"""
        while True:
            try:
                choice = input("\nPlease select voice number (1-{0}) or press Enter to use current voice: ".format(
                    len(self.female_chinese_voices)))

                if not choice.strip():
                    return self.current_voice

                choice_num = int(choice)
                if 1 <= choice_num <= len(self.female_chinese_voices):
                    return self.female_chinese_voices[choice_num - 1]['short_name']
                else:
                    print(
                        f"❌ Please enter a number between 1-{len(self.female_chinese_voices)}")

            except ValueError:
                print("❌ Please enter a valid number")

    def switch_voice(self, voice_name: str) -> bool:
        """Switch voice"""
        if not self.tts_provider:
            print("❌ TTS provider not initialized")
            return False

        if self.tts_provider.set_voice(voice_name):
            self.current_voice = voice_name
            # Find display name
            display_name = voice_name
            for voice in self.female_chinese_voices:
                if voice.get('short_name') == voice_name:
                    display_name = voice.get(
                        'local_name', voice.get('display_name', voice_name))
                    break
            print(f"✅ Voice switched to: {display_name}")
            return True
        else:
            print("❌ Voice switch failed")
            return False

    async def test_voice(self, voice_name: str) -> bool:
        """Test voice"""
        if not self.tts_provider:
            print("❌ TTS provider not initialized")
            return False

        try:
            print("🔊 Testing voice...")
            test_text = "This is a voice test to verify that the selected voice works properly."

            # Synthesize audio
            audio_data = await self.tts_provider.synthesize(test_text, voice=voice_name)

            # Play audio
            await self.tts_provider.play_audio(audio_data)

            print("✅ Voice test completed")
            return True

        except Exception as e:
            print(f"❌ Voice test failed: {e}")
            return False

    async def run_interactive_demo(self) -> None:
        """Run interactive demo"""
        print("🎤 Edge-TTS Voice Selector Demo")
        print("=" * 50)

        # Initialize
        if not await self.initialize():
            return

        while True:
            # Display voice list
            self.display_voice_list()

            # Get user choice
            selected_voice = self.get_voice_choice()

            if selected_voice != self.current_voice:
                # Switch voice
                if not self.switch_voice(selected_voice):
                    continue
            else:
                print("ℹ️ Continue using current voice")

            # Test voice
            await self.test_voice(selected_voice)

            # Ask if continue
            choice = input(
                "\nDo you want to test other voices? (y/N): ").strip().lower()
            if choice not in ['y', 'yes']:
                break

        print("\n👋 Demo ended")


async def main():
    """Main function"""
    demo = VoiceSelectorDemo()
    await demo.run_interactive_demo()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 User interrupted")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

