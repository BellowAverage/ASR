from paddlespeech.cli.tts.infer import TTSExecutor

def tts_execute(gpt_response):
    tts = TTSExecutor()
    tts(text=gpt_response, output="output.wav")