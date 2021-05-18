import pandas as pd
import random
import time
from random import choice
name_list = ['Rex', 'Evelyn', 'Chloe', 'Tom', 'Sam']
region_list=['台北', '台中', '台南']
product_list = ['Iphone', 'HTC', 'Samsung']
name = []
region = []
product = []
date = []
income = []

a1=(2020,1,1,0,0,0,0,0,0) #設置開始日期時間元組（1976-01-01 00：00：00）
a2=(2020,12,31,23,59,59,0,0,0) #設置結束日期時間元組（1990-12-31 23：59：59）
start=time.mktime(a1) #生成開始時間戳
end=time.mktime(a2) #生成結束時間戳


for i in range(0, 100):
    name.append(choice(name_list))
    region.append(choice(region_list))
    product.append(choice(product_list))
    t = random.randint(start, end)  # 在開始和結束時間戳中隨機取出一個
    day_touple = time.localtime(t)  # 將時間戳生成時間元組
    day = time.strftime("%Y年%m月%d日", day_touple)  # 將時間元組轉成格式化字符串（1976-05-21）
    date.append(day)
    income.append(random.randint(100, 500))


df = pd.DataFrame({'銷售員': name, '地區': region, '產品': product, '日期': date, '銷售金額': income})
# df['date'] = df['date'].str.split('-').str.get(0)#抓出年月日




print(df)
df.to_csv('sales_data.csv', encoding='big5')

