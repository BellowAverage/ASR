import chat_response
import recognize
import tts_executor
from playsound import playsound
import audio_recording

def main():
    audio_recording.start_audio(5, "zh.wav")
    str_in = recognize.recognize("zh.wav")
    # str_in = recognize.recognize(r"m4a/workplace_record_1.wav")
    print("recognized_result: ", str_in)
    print("requesting from ChatGPT ...")

    # response = chat_response.single_response(str_in)
    response = chat_response.multi_response(str_in)
    print("chatgpt_response", response)

    tts_executor.tts_execute(response)
    playsound("output.wav")
    print("sound playing ...")


if __name__ == '__main__':
    main()
