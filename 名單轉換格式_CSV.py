import csv

# 開啟輸出的 CSV 檔案。如果檔案不存在，將會創建一個新檔案。
with open('yourOutput.csv', 'w', newline='') as csvFile:
    # 建立 CSV 檔案的寫入器，用於將資料寫入 CSV 格式。
    writer = csv.writer(csvFile)
    # 寫入標題行，這裡是 '@Name'。
    writer.writerow(['@Name'])

# 從使用者那裡讀取輸入。
raw = input()

# 把輸入按空格分割，儲存到名單列表中。
name = raw.split()
# 初始化一個長度為 16 的數字列表，用於儲存不同編號的計數。
number = [0] * 16
# 初始化一個長度為 16 的計數列表，用於計算每個編號對應的名字數量。
count = [0] * 16

print("邀請卡名單 \n")

# 遍歷名單中的每個元素。
for i in name:
    # 如果元素是數字，將其轉換為整數並儲存到 nowNum 變數中。
    if i.isdigit():
        nowNum = int(i)
    else:
        # 如果元素不是數字，增加對應編號的計數，並將名字打印出來。
        count[nowNum] += 1
        print(i)
        # 將名字寫入 CSV 檔案。
        writer.writerow([i])

print("\n----------\n")

# 遍歷 0 到 15 的數字。
for i in range(len(number)):
    # 如果某個編號對應的計數不為零，則打印出該編號和對應的邀請卡數量。
    if count[i] != 0:
        print("{:<2}號：{:^3}張邀請卡".format(i, count[i]))

# 關閉 CSV 檔案。
csvFile.close()
