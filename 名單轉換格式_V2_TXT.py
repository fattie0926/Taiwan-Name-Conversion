# 打開用於寫入的文本檔案 'Raw Name List.txt' 和 'Raw Duplicate Name List.txt'。
f = open('Raw Name List.txt', 'w')
fd = open('Raw Duplicate Name List.txt', 'w')
print("邀請名單轉換程式\nCopyright © 2020 Jaron Wong (王則倫). All rights reserved.")

# 從使用者那裡獲取班級的學生人數。
studentNumber = int(input("請問貴班人數：\n")) + 1
# 從使用者那裡獲取學生和學校的表單內容。
rawData = input("請輸入學生表單內容\n")
schoolData = input("請輸入學校名單\n")

# 將原始資料和學校資料按空格分割。
rawData = rawData.split()
schoolData = schoolData.split()
# 初始化計數列表，長度為學生人數。
count = [0] * studentNumber
# 創建列表來存儲唯一的名字和重複的名字。
nameOnlyList = []
nameDuplicateList = []
schoolNameDuplicateList = []
printNewLineCount = 0
nameDuplicateExport = []

print("\n-----學生邀請卡名單-----\n")

# 遍歷原始資料中的每個元素。
for i in rawData:
    if i.isdigit():
        nowNum = int(i)
    else:
        if i not in nameOnlyList:
            count[nowNum] += 1
            nameOnlyList.append(i)
            print(i, end=' ')
            printNewLineCount += 1
            if printNewLineCount == 15:
                print()
                printNewLineCount = 0
        else:
            # 如果名字重複，記錄重複的名字和對應的編號。
            for j in range(rawData.index(i), 0, -1):
                if rawData[j].isdigit():
                    nameDuplicateList.append(rawData[j])
                    break
            nameDuplicateList.append(nowNum)
            nameDuplicateList.append(i)

print("\n-----學校邀請卡名單-----\n")

# 遍歷學校資料，處理重複的名字。
for i in schoolData:
    if i not in nameOnlyList:
        count[0] += 1
        nameOnlyList.append(i)
        print(i, end=' ')
        printNewLineCount += 1
        if printNewLineCount == 15:
            print()
            printNewLineCount = 0
    else:
        schoolNameDuplicateList.append(i)

# 處理名單中重複的名字。
if nameDuplicateList:
    print("\n-----名單重複者-----\n")
    for k in range(0, len(nameDuplicateList), 3):
        if nameDuplicateList[k] != 0:
            print("{:<2}和{:<2}重複邀請了：{}".format(nameDuplicateList[k], nameDuplicateList[k + 1], nameDuplicateList[k + 2]), end='')
            addDuplicate = input("要新增到名單嗎？ y/n\n")
            if addDuplicate == "y":
                nameDuplicateExport.append(nameDuplicateList[k + 2])
                print("*已新增「{}」*\n".format(nameDuplicateList[k + 2]))
                count[nameDuplicateList[k + 1]] += 1
            elif addDuplicate == "n":
                print("*已略過「{}」*\n".format(nameDuplicateList[k + 2]))
            else:
                print("*錯誤輸入，視為不加入*")

# 處理學校名單中重複的名字。
if schoolNameDuplicateList:
    for k in schoolNameDuplicateList:
        print("學校重複邀請了：{}".format(k), end='')
        addDuplicate = input("要新增到名單嗎？ y/n\n")
        if addDuplicate == "y":
            nameDuplicateExport.append(k)
            count[0] += 1
            print("*已新增「{}」*\n".format(k))
        elif addDuplicate == "n":
            print("*已略過「{}」*\n".format(k))
        else:
            print("*錯誤輸入，視為不加入*")

print("\n-----每人邀請人數統計-----\n")

# 統計和打印每個人的邀請卡數量。
for i in range(0, studentNumber):
    if i != 0 and count[i] != 0:
        print("{:^2}號：{:<2}張邀請卡".format(i, count[i]))
    elif i == 0:
        print("學校：{:<2}張邀請卡".format(count[i]))
    else:
        print("** {:^2}號未邀請 **".format(i))
print("\n=====共", len(nameOnlyList), "張=====")

print("\n寫入資料中...")
# 將名單寫入文件。
for i in nameOnlyList:
    f.write(i + '\n')
for i in nameDuplicateExport:
    fd.write(i + '\n')

print("\n已輸出\nRaw Name List.txt 和\nRaw Duplicate Name List.txt")

# 程序執行完畢，關閉文件。
print("\n程序執行完畢\nCopyright © 2020 Jaron Wong (王則倫). All rights reserved.")
f.close()
fd.close()
