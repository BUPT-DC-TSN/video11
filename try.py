from paddleocr import PaddleOCR, draw_ocr
import os
folder_path = "frames"
# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="en")  # need to run only once to download and load model into memory
for root, dirs, files in os.walk(folder_path):
    # 打印当前目录路径
    # 打印当前目录下的所有文件路径
    for file in files:
        file_path = os.path.join(root, file)
        print(file_path)
        result = ocr.ocr(file_path, cls=True)
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                print(line[1][0])
                result = line[1][0]
                with open("output.txt", "a",) as file:
                    file.write(result+'\n')