import chat_response
import recognize


def main():
    str_in = recognize.recognize("zh.wav")
    print(str_in)
    response = chat_response.single_response(str_in)
    print(response)


if __name__ == '__main__':
    main()
