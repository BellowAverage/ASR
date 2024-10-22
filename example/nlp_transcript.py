import re


def remove_inner_spaces(text):
    lines = text.split('\n')  # 按行拆分文本
    for i in range(len(lines)):
        line = lines[i]
        match = re.search(r'(BAC\S+)\s+([\u4e00-\u9fa5])', line)  # 匹配编号和汉字之间的空格
        if match:
            start_index = match.start()
            end_index = match.end()
            content = line[end_index:]  # 获取空格后的内容
            updated_content = re.sub(r'\s+', '', content)  # 删除内容之间的空格
            lines[i] = line[:end_index] + updated_content
    return '\n'.join(lines)  # 连接文本并返回


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


file_path = 'aishell_transcript_v0.8.txt'
document = read_file(file_path)
result = remove_inner_spaces(document).replace('    ', ' ').replace('  ', ' ')
# result = replace_multiple_spaces(result)
write_to_file("output.txt", result)
