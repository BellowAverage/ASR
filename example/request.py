import requests


def send_request_to_django():
    # Django服务器的URL
    django_url = "http://124.222.120.214/ai_voice_assistant_handle/hi"
    # django_url = "http://124.222.120.214/index"

    try:
        # 发送GET请求到Django服务器
        response = requests.get(django_url)

        # 检查响应状态码
        print(response.status_code)
        if response.status_code == 200:
            # 获取返回的文本数据
            response_text = response.text
            return response_text
        else:
            print(f"Request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")


if __name__ == "__main__":
    returned_text = send_request_to_django()
    if returned_text:
        print("Returned text from Django server:")
        print(returned_text)
