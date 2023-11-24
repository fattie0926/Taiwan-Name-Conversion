# 打開一個用於寫入的文本檔案 'Raw Name List.txt'。
f = open('Raw Name List.txt', 'w')

# 從使用者那裡獲取班級的學生人數。
studentNumber = int(input("請問貴班人數：\n")) + 1
# 從使用者那裡獲取原始的表單內容。
rawData = input("請輸入表單內容\n")

# 將原始資料按空格分割。
rawData = rawData.split()
# 初始化計數列表，長度為學生人數。
count = [0] * studentNumber
# 創建一個列表來存儲唯一的名字。
nameOnlyList = []
# 創建一個列表來存儲重複的名字和對應的編號。
nameDuplicateList = []

print("\n-----邀請卡名單-----\n")

# 遍歷原始資料中的每個元素。
for i in rawData:
    # 如果元素是數字，將其轉換為整數並儲存到 nowNum 變數中。
    if i.isdigit():
        nowNum = int(i)
    else:
        # 如果名字不在 nameOnlyList 中，則加入該名單並更新計數。
        if i not in nameOnlyList:
            count[nowNum] += 1
            nameOnlyList.append(i)
            print(i)
            # 將名字寫入文本檔案。
            f.write(i + '\n')
        else:
            # 如果名字已存在於 nameOnlyList 中，則尋找並記錄重複的名字和對應的編號。
            for j in range(rawData.index(i), 0, -1):
                if rawData[j].isdigit():
                    nameDuplicateList.append(rawData[j])
                    break
            nameDuplicateList.append(nowNum)
            nameDuplicateList.append(i)

print("\n-----每人邀請人數統計-----\n")

# 遍歷學生編號，打印每個人的邀請卡數量。
for i in range(0, studentNumber):
    if count[i] != 0:
        print("{:^2}號：{:<2}張邀請卡".format(i, count[i]))
    elif i == 0:
        print("學校：{:<2}張邀請卡".format(count[i]))
    else:
        print("** {:^2}號未邀請 **".format(i))
print("\n共", len(nameOnlyList), "張")

# 如果有重複邀請的情況，則打印出重複的名字和對應的編號。
if nameDuplicateList:
    print("\n-----名單重複者-----\n")
    for k in range(0, len(nameDuplicateList), 3):
        print("{:<2}和{:<2}重複邀請了：{}".format(nameDuplicateList[k], nameDuplicateList[k + 1], nameDuplicateList[k + 2]))

# 關閉文本檔案。
f.close()
