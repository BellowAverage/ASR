import soundfile
from espnet_model_zoo.downloader import ModelDownloader
from espnet2.bin.asr_inference import Speech2Text

def recognize(wav_audio):
    d = ModelDownloader()
    speech2text = Speech2Text(
    **d.download_and_unpack("kamo-naoyuki/aishell_conformer"),
        # Decoding parameters are not included in the model file
        maxlenratio=0.0,
        minlenratio=0.0,
        beam_size=20,
        ctc_weight=0.3,
        lm_weight=0.5,
        penalty=0.0,
        nbest=1
    )
    audio, rate = soundfile.read(wav_audio)
    nbests = speech2text(audio)
    text, *_ = nbests[0]
    return str(text)