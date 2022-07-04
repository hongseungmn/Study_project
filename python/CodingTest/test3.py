#주차장의 요금표와 차량이 들어오고(입차) 나간(출차) 기록이 주어졌을 때, 
# 차량별로 주차 요금을 계산하려고 합니다.


from time import strptime
import pandas as pd
from datetime import datetime

# fees =[180, 5000, 10, 600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", 
#             "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", 
#             "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
fees =[120, 0, 60, 591] 
records = ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]

    

df = pd.DataFrame(columns=["time","carNum","state"])

for record in records:
    record = record.split()
    df.loc[len(df)] = record

df_dup = df.drop_duplicates(["carNum"])
df_dup_list = list(df_dup["carNum"])
print(sorted(df_dup_list))
df_dup_list = sorted(df_dup_list)



answer =[]
for num in df_dup_list:
    carInOut = df[df.carNum == num]
    carInOut = carInOut.reset_index(drop=True)
    print(carInOut)
    useTime=0
    if (len(carInOut) % 2 ==1):
        carInOut.loc[len(carInOut)] = ["23:59",num,0]
    print(carInOut)
    for i in range(0,len(carInOut),2):
        sumTime = datetime.strptime(carInOut.iloc[i+1]["time"],"%H:%M") - datetime.strptime(carInOut.iloc[i]["time"],"%H:%M")
        useTime += sumTime.seconds//60

    print(useTime)
    
    if(useTime > fees[0]):
        if (useTime%fees[2])>0:
            useTime += (fees[2] - (useTime%fees[2]))
        answer.append(fees[1]+ (useTime - fees[0])*(fees[3]/fees[2]))
    else:
        answer.append(fees[1])
print(answer)