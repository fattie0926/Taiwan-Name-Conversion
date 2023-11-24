# 打開用於讀取的文本檔案 'Raw Name List.txt'。
f = open('Raw Name List.txt', 'r')
print("外交部姓名中英譯系統轉換\nCopyright © 2020 Jaron Wong (王則倫). All rights reserved.\n")

# 讀取檔案的所有行。
rawLines = f.readlines()
# 初始化名字列表和其他變數。
nameList = []
printLimit = 0
printTimeCount = 0

# 初始化用於存儲轉換後名字的列表。
nameWithTrans = []
transList = [["name"]]
count = 1
flag = True
rawTransList = []

# 將每行的名字去除空白並加入名字列表。
for i in rawLines:
    nameList.append(i.strip())

# 打印名字並在達到一定數量後要求輸入轉換後的名字。
for j in nameList:
    for k in range(len(j)):
        if k != (len(j) - 1):
            print("{},".format(j[k]), end='')
        else:
            print("{};".format(j[k]), end='')
            printLimit += 1
    if printLimit % 200 == 0 or ((len(nameList) - printLimit) < 200 and j == nameList[-1]):
        printTimeCount += 1
        rawTrans = input("請輸入")
        rawTransListTemp = rawTrans.split()
        for o in rawTransListTemp:
            rawTransList.append(o)

# 處理轉換列表中的 '或' 字樣。
while flag == True:
    if "或" in rawTransList:
        del rawTransList[rawTransList.index("或") + 1]
        rawTransList.remove("或")
    else:
        flag = False

flag = True

# 處理並存儲轉換後的名字。
for m in range(0, len(rawTransList), 7):
    if rawTransList[m + 1] in nameList:
        transList.append([])
        nowAppend = rawTransList[m + 1] + " " + rawTransList[m + 3]
        transList[count].append(nowAppend)
        nameList.remove(rawTransList[m + 1])
        count += 1

print("\n寫入資料中...")

# 將轉換後的名字寫入 CSV 檔案。
import csv
with open('Data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(transList)

# 程序結束提示。
print("\n*Raw Duplicate Name.txt中的名單, 記得複製到新的CSV\n\n程序執行完畢\nCopyright © 2020 Jaron Wong (王則倫). All rights reserved.")
