import csv
import re

# 原始 CSV 文件路径（即 12.7.csv）
input_csv = 'ROC_result_filtered9.csv'
# 输出的清洗后 CSV 文件路径
output_csv = '12.7_90_clean.csv'

# 正则表达式，用于匹配带有 `us` 的数字（包括整数和浮动数字）
pattern = r"(\d+(\.\d+)?)(us|ms|ns)"


# 函数：将数值从字符串转换为浮动数，并返回数值大小
def parse_value(value):
    return float(value)


# 读取原始 CSV 文件并处理数据
with open(input_csv, mode='r', encoding='utf-8') as infile, open(output_csv, mode='w', newline='',
                                                                 encoding='utf-8') as outfile:
    # 创建 CSV 阅读器和写入器
    reader = csv.DictReader(infile)
    fieldnames = ['Filename', 'OCR_Result']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    # 写入 CSV 表头
    writer.writeheader()

    # 存储符合条件的结果
    ocr_values = []  # 用来存储所有的数值（已转换为浮动数）
    rows = []  # 用来存储原始的行数据（文件名与OCR结果）

    # 先获取所有 OCR 结果的数值，并保留相关信息
    for row in reader:
        filename = row['Filename']
        ocr_result = row['OCR_Result']

        match = re.search(pattern, ocr_result)

        if match:
            value = match.group(1)  # 提取数字部分
            parsed_value = parse_value(value)

            if parsed_value is not None:
                ocr_values.append(parsed_value)
                rows.append((filename, ocr_result, parsed_value))

    # 遍历所有的 OCR 数值，保留大于前一个且小于后一个的数值
    valid_rows = []
    for i in range(1, len(ocr_values) - 1):
        prev_value = ocr_values[i - 1]
        current_value = ocr_values[i]
        next_value = ocr_values[i + 1]

        # 比较当前数值是否大于前一个且小于后一个
        if prev_value < current_value < next_value:
            valid_rows.append(rows[i])  # 只保留符合条件的行

    # 将符合条件的数据写入输出 CSV 文件
    for filename, result, _ in valid_rows:
        writer.writerow({'Filename': filename, 'OCR_Result': result})

    print(f"清洗后的数据已保存到 {output_csv} 文件中。")
