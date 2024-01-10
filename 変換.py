import codecs

def convert_encoding(input_file, output_file):
    with codecs.open(input_file, 'r', 'Shift_JIS') as f:
        html_content = f.read()

    with codecs.open(output_file, 'w', 'utf-8') as f:
        f.write(html_content)

# 使用例
convert_encoding('input.html', 'output.html')
