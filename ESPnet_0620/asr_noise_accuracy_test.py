# coding=utf-8

import time
from jiwer import wer, cer, mer, wil
from recognize import recognize
import csv
import os


def get_all_filenames(folder_path):
    filenames = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            filenames.append(file)
    return filenames


# 模拟ASR系统的识别函数
def recognize_speech(audio):
    # 返回识别结果的文本
    return recognize(audio)


def search_value_in_file(filename, target_value):
    with open(filename, 'r') as file:
        for line in file:
            if target_value in line:
                return line.strip()
    return None


def delete_text_before(text, target_text):
    index = str(text).find(target_text)
    if index != -1:
        return text[index + len(target_text):]
    else:
        return text


# 模拟ASR测试的语音数据
test_audio = []
reference_text = []

all_folder_path = []
folder_path_1 = "/home/chriswang/ASR/_Accuracy_0627/data/wav/S0002/train/S0002/"
folder_path_2 = "/home/chriswang/ASR/_Accuracy_0627/data/wav/S0002/train/S0003/"
all_folder_path.append(folder_path_1)
all_folder_path.append(folder_path_2)

for folder_path in all_folder_path:
    file_names = get_all_filenames(folder_path)
    filename = '/home/chriswang/ASR/_Accuracy_0627/data/transcript/nlp_processed_transcript.txt'

    for file_name in file_names:
        print(file_name)
        print(file_name.replace(".wav", ""))
        test_audio.append(folder_path + file_name)
        reference_text_conciser = delete_text_before(search_value_in_file(filename, file_name.replace(".wav", "")), " ")
        reference_text.append(reference_text_conciser)

# 用于存储结果的变量
total_wer = 0
total_transcriptions = 0
total_processing_time = 0

# 存储结果
results = []

# 遍历每个语音样本进行测试
for audio_path, reference in zip(test_audio, reference_text):
    # 测量识别时间
    start_time = time.time()

    # 对语音进行识别
    transcription = recognize_speech(audio_path)

    # 计算识别时间
    processing_time = time.time() - start_time

    # 计算词错误率（Word Error Rate）
    error_rate = cer(reference, transcription)
    try:
        error_rate = cer(reference, transcription)
    except ValueError:
        error_rate = 1

    # 其他指标 - 弃用
    try:
        mer_error = mer(reference, transcription)
        wil_error = wil(reference, transcription)
    except ValueError:
        mer_error = 0
        wil_error = 0

    # average time per character
    tpc = processing_time / len(transcription)

    # 输出结果
    print("Reference:", reference)
    print("Transcription:", transcription)
    # print("WER:", error_rate)
    print("CER:", error_rate)
    print("Processing time:", processing_time, "seconds")
    print("Time per Char:", tpc, "seconds/character\n")

    # 将结果添加到列表中
    audio_path_conciser = delete_text_before(audio_path, "train/")
    results.append({
        "Audio": audio_path_conciser,
        "Reference": reference,
        "Transcription": transcription,
        "CER": error_rate,
        "MER": mer_error,
        "WIL": wil_error,
        "ProcessingTime": processing_time,
        "Time per Char": tpc,
    })

    # 累计结果
    total_wer += error_rate
    total_transcriptions += 1
    total_processing_time += processing_time

# 计算平均指标
average_wer = total_wer / total_transcriptions
average_processing_time = total_processing_time / total_transcriptions

# 输出平均指标结果
print("Average WER:", average_wer)
print("Average processing time:", average_processing_time, "seconds")

# 将结果写入CSV文件
output_file = "results.csv"

with open(output_file, mode='w', newline='') as file:
    fieldnames = ["Audio", "Reference", "Transcription", "CER", "MER", "WIL", "ProcessingTime", "Time per Char"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # 写入表头
    writer.writeheader()

    # 逐行写入结果
    for result in results:
        writer.writerow(result)

print("Results saved to", output_file)
