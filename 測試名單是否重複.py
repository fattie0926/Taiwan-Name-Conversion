# 從使用者那裡獲取原始數據。
rawData = input()
# 將原始數據按空格分割，轉換成列表。
rawData = rawData.split()

# 初始化一個空列表來存儲唯一的名字。
nameList = []

# 遍歷分割後的數據。
for i in rawData:
    # 如果當前元素不在名字列表中，則加入該列表。
    if i not in nameList:
        nameList.append(i)
    else:
        # 如果元素已經存在於名字列表中，則打印出來。
        print(i)
