import pandas as pd

# 讀取 EXCEL 文件
df1 = pd.read_csv('112年1-10月交通事故簡訊通報資料.csv')

df1['國道名稱'] = df1['國道名稱'].fillna('')
df1 = df1[df1['國道名稱'].str.contains('國道1號')]
df1 = df1[df1['方向'].str.contains('南|南向')]

#把 欄位 '年' '月' '日' '時' '分'
#合併成一個欄位 '日期' , 並且轉換成日期格式
df1['事件開始'] = df1['年'].astype(str) + '-' + df1['月'].astype(str) + '-' + df1['日'].astype(str) + ' ' + df1['時'].astype(str) + ':' + df1['分'].astype(str)
df1['事件開始'] = pd.to_datetime(df1['事件開始'])

#把 欄位 '年' '月' '日' '事件排除'  合併成一個欄位 '事件排除' , 並且轉換成日期格式
df1['事件排除'] = df1['年'].astype(str) + '-' + df1['月'].astype(str) + '-' + df1['日'].astype(str) + ' ' + df1['事件排除'].astype(str)
df1['事件排除'] = pd.to_datetime(df1['事件排除'])

#drop 欄位 '年' '月' '日' '時' '分'
df1 = df1.drop(columns=['年', '月', '日', '時', '分'])

#將 '事件開始' '事件排除' 兩個欄位轉換成 unix time stamp 並使用整數表示
import pandas as pd

#假設 df 是您的 DataFrame，並且 '事件開始' 和 '事件排除' 是 datetime 欄位

df1['事件開始1'] = df1['事件開始'].apply(lambda x: int(x.timestamp()))
df1['事件排除1'] = df1['事件排除'].apply(lambda x: int(x.timestamp()))

#只印出 '事件開始' '事件排除' '國道名稱' '事件類型' '事件描述'
print(df1[['事件開始', '事件排除', '國道名稱', '里程', '事件開始1', '事件排除1']])

#以 '里程' 為y軸 , '事件開始1' 為 x軸 起點 , '事件排除1' 為 x軸 終點 繪製線段
import matplotlib.pyplot as plt

# 假設 df 是您的 DataFrame
for index, row in df1.iterrows():
    plt.plot([row['事件開始1'], row['事件排除1']], [row['里程'], row['里程']])

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xlabel('事件時間')
plt.ylabel('里程')
plt.title('11022348, 國道一號南向')
plt.show()

#國道一號南向, 國道一號北向, 國道三號南向, 國道三號北向

