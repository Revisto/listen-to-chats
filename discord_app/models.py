class Discord:
    def current_voice_channel_in(self, ctx):
        try:
            voice_channel = ctx.me.voice.channel
            return voice_channel
        except AttributeError:
            return None

    def play_audio(self, discord, vc, audio_path):
        vc.play(discord.FFmpegPCMAudio(audio_path), after=lambda e: print('done playing audio', e))
