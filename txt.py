import csv
import re

# 原始 CSV 文件路径（即 12.7.csv）
input_csv = '12.7_90.csv'
# 输出的清洗后 CSV 文件路径
output_csv = 'ROC_result_filtered9.csv'

# 正则表达式，用于匹配带有 `us` 或 `ms` 的数字（包括整数和浮动数字）
pattern = r"(\d+(\.\d+)?)(us|ms|ns)"

# 读取原始 CSV 文件并处理数据
with open(input_csv, mode='r', encoding='utf-8') as infile, open(output_csv, mode='w', newline='',
                                                                 encoding='utf-8') as outfile:
    # 创建 CSV 阅读器和写入器
    reader = csv.DictReader(infile)
    fieldnames = ['Filename', 'OCR_Result']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    # 写入 CSV 表头
    writer.writeheader()

    # 遍历每一行数据
    for row in reader:
        filename = row['Filename']
        ocr_result = row['OCR_Result']

        # 使用正则表达式查找 OCR 结果中包含 `us` 或 `ms` 的数字
        match = re.search(pattern, ocr_result)

        # 如果匹配到了有效的数字（例如：12us、45ms、12.5ms）
        if match:
            # 提取匹配的内容并写入新的 CSV 文件
            writer.writerow({'Filename': filename, 'OCR_Result': match.group()})

    print(f"清洗后的数据已保存到 {output_csv} 文件中。")

