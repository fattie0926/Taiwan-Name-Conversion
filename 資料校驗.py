import csv

# 打開並讀取 'Raw Name List.txt' 文件的內容。
f = open('Raw Name List.txt', 'r')
rawLines = f.readlines()
# 在讀取到的行列表的開頭插入一個元素。
rawLines.insert(0, 'name|')

# 打開 CSV 檔案 'Data.csv' 用於讀取。
with open('Data.csv', newline='') as csvfile:
    # 使用 csv 模塊創建一個 reader 對象。
    rows = csv.reader(csvfile)

    # 初始化計數器。
    count = 0

    # 遍歷 CSV 檔案的每一行。
    for row in rows:
        # 打印當前行的第一個元素和對應的 rawLines 列表中的元素。
        print(row[0], rawLines[count], end='')
        # 更新計數器。
        count += 1

# 關閉文本文件。
f.close()
