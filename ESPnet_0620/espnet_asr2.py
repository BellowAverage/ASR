import soundfile
from espnet_model_zoo.downloader import ModelDownloader
from espnet2.bin.asr_inference import Speech2Text
d = ModelDownloader()
speech2text = Speech2Text.from_pretrained(
**d.download_and_unpack("espnet/owsm_v3"),
    # Decoding parameters are not included in the model file
    
    train_config="/home/chriswang/ASR/ESPnet_0620/venv/lib/python3.10/site-packages/espnet_model_zoo/models--espnet--owsm_v3/snapshots/9813a6782603ea6049776832e59a1984ec708326/exp/s2t_train_s2t_transformer_conv2d_size1024_e24_d24_lr2.5e-4_warmup10k_finetune_raw_bpe50000/config.yaml",
    model_file="/home/chriswang/ASR/ESPnet_0620/venv/lib/python3.10/site-packages/espnet_model_zoo/models--espnet--owsm_v3/snapshots/9813a6782603ea6049776832e59a1984ec708326/exp/s2t_train_s2t_transformer_conv2d_size1024_e24_d24_lr2.5e-4_warmup10k_finetune_raw_bpe50000/valid.acc.ave_5best.till50epoch.pth",
    
    maxlenratio=0.0,
    minlenratio=0.0,
    beam_size=20,
    ctc_weight=0.3,
    lm_weight=0.5,
    penalty=0.0,
    nbest=1
)
audio, rate = soundfile.read("5.wav")
nbests = speech2text(audio)
text, *_ = nbests[0]
print(text)

