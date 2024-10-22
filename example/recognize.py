from paddlespeech.cli.asr.infer import ASRExecutor

def recognize(audio):
    asr = ASRExecutor()
    result = asr(audio_file=audio)
    # result = asr(audio_file="audio.m4a")
    return result