from GetLOL import LOL # 爬虫主体
import csv
import os
import pandas as pd
#lpl夏季赛从32216开始，到34142截至，中间存在其他竞赛信息
#---------------------------------------------------------#
csv_team='team_data'
csv_player='player_data'

#for i in range(32216,34142): 其中20787到20793都无法访问 23848到
for i in range(20849,34142): #爬取所有比赛记录
    try:
        lol = LOL(str(i))  # 初始化得到所有数据
        #爬取所有战队，保存到csv_team
        # 列索引： 编号 战队名 胜负 日期 mvp 时间 小龙 大龙 推塔 杀人 死亡 助攻 经济
        BaseTeam = lol.GetBaseInfo()
        data0 = pd.DataFrame(BaseTeam)
        data0.to_csv('data/'+csv_team+'.csv',mode='a',index = False ,header=False) #追加写入不要索引
        print(data0)

        #这里爬取所有选手 保存到csv_player
        BasePlayer = lol.GetPlayerInfo()
        data1 = pd.DataFrame(BasePlayer)
        data1.to_csv('data/'+csv_player+'.csv',mode='a',index = False ,header=False) #追加写入不要索引
        print(data1)
        #print(BaseTeam)
    except:
        print("这里出错了，pass")

