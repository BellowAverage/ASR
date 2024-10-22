import soundfile
from espnet_model_zoo.downloader import ModelDownloader
from espnet2.bin.asr_inference import Speech2Text
import numpy as np

def recognize_long_audio(wav_audio, chunk_size=30.0):
    # Load the ASR model
    d = ModelDownloader()
    speech2text = Speech2Text(
       #**d.download_and_unpack("kamo-naoyuki/aishell_conformer"),
       **d.download_and_unpack("espnet/owsm_v3"),
       #**d.download_and_unpack("kamo-naoyuki/chime4_asr_train_asr_transformer3_raw_en_char_sp_valid.acc.ave"),
        maxlenratio=0.0,
        minlenratio=0.0,
        beam_size=30,
        ctc_weight=0,
        # ctc_weight=0.3,
        lm_weight=0.5,
        penalty=0.0,
        nbest=1
    )

    # Read the entire audio file
    audio, rate = soundfile.read(wav_audio)

    # Split the audio into chunks
    chunk_size_samples = int(chunk_size * rate)
    num_chunks = int(np.ceil(len(audio) / chunk_size_samples))

    # Process each chunk and concatenate the results
    recognized_texts = []
    for i in range(num_chunks):
        start_sample = i * chunk_size_samples
        end_sample = min((i + 1) * chunk_size_samples, len(audio))
        chunk = audio[start_sample:end_sample]

        # Print information about the current chunk
        print(f"Processing chunk {i + 1}/{num_chunks}, duration: {len(chunk) / rate:.2f} seconds")

        # Perform ASR on the chunk
        nbests = speech2text(chunk)

        # Get the text from the best result
        text, *_ = nbests[0]
        recognized_texts.append(text)

    # Combine the recognized texts from all chunks
    print("current: ", recognized_texts)
    result_text = ' '.join(recognized_texts)
    return result_text

# Example usage
try:
    recognized_text = recognize_long_audio("5.wav")
    print("Recognition successful:")
    print(recognized_text)
except Exception as e:
    print("Error during recognition:")
    print(e)

