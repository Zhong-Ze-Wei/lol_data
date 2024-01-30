'''
本文件用于英雄联盟赛事数据爬取
预计爬取内容为选手单场数据、战队数据、英雄数据、装备数据
选手单场数据： 选手名，时间，赛季，战队，对战，英雄，kda，召唤师技能，符文，
'''
#-------------------载入库--------------------------------------#
import requests
import json
from lxml import etree
import re
#--------------------载入url-------------------------------------#
def get_info(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}
    response = requests.get(url=url,headers=headers)
    return response.text
#lpl夏季赛从32216开始，到34142截至

# -------------------代码区域--------------------------------------#
class LOL:
    '贴吧爬虫，负责爬取该吧中的相关信息'
    def __init__(self,num):
        self.num=num
        self.info_team = get_info('https://img.scoregg.com/match/result/'+num+'.json?_=1660730052072')
        print('https://img.scoregg.com/match/result/'+num+'.json?_=1660730052072')
        self.info = json.loads(self.info_team)['data']  # 将str对象转换为dict（字典）对象

    def GetBaseInfo(self):
        #此命令返回该局比赛的基本情况
        date=self.info['updated_at']
        winner_club=self.info['max_mvp']['team_name']
        loser_club=self.info['max_beiguo']['team_name']
        mvp=self.info['max_mvp']['nickname']

        info = self.info['result_list']
        time=str(info['game_time_m']+info['game_time_s'])

        red_name=info['red_name']
        red_result=info['red_result']
        red_small_dargon=info['red_small_dargon']
        red_big_dargon=info['red_big_dargon']
        red_tower=info['red_tower']
        red_kill=info['red_kill']
        red_die=info['red_die']
        red_asses=info['red_asses']
        red_money=info['red_money']

        blue_name=info['blue_name']
        blue_result=info['blue_result']
        blue_small_dargon=info['blue_small_dargon']
        blue_big_dargon=info['blue_big_dargon']
        blue_tower=info['blue_tower']
        blue_kill=info['blue_kill']
        blue_die=info['blue_die']
        blue_asses=info['blue_asses']
        blue_money=info['blue_money']
        # 比赛编号，红方战队，红方胜负，日期，mvp归属，时间，红方小龙，红方大龙，红方推塔，红方击杀，红方死亡，红方助攻，红方经济
        baseInfo=[[self.num,
                  red_name,
                  red_result,
                  date,
                  mvp,
                  time,
                  red_small_dargon,
                  red_big_dargon,
                  red_tower,
                  red_kill,
                  red_die,
                  red_asses,
                  red_money],
                  [self.num,
                  blue_name,
                  blue_result,
                  date,
                  mvp,
                  time,
                  blue_small_dargon,
                  blue_big_dargon,
                  blue_tower,
                  blue_kill,
                  blue_die,
                  blue_asses,
                  blue_money]]

        if is_chinese(red_name)and is_chinese(blue_name):
            return 0
        else:
            return baseInfo


    def GetPlayerInfo(self):
        #此函数返回该局比赛十位队员的情况
        info=self.info['result_list']
        list=['a','b','c','d','e']
        list2=['name','kda','kills','deaths','assists',
               'part','atk','atk_o','atk_p','atk_m',
               'def','def_o','def_p','def_m',
               'adc_m','money','money_o','money_M','wp_m','hits'] #加在后面的属性：比赛编号，team_name，比赛位置，红蓝方，比赛时间，获胜情况
        player=[]
        players=[]

        for team in ['red','blue']:
            for weizhi in list:
                #hero=team+'_hero_'+num+'_' #前缀确定
                #player.append(info[hero+'name'])

                star=team+'_star_'+weizhi+'_' #前缀确定
                for data in list2:
                    #print(star+data) 写入的属性
                    player.append(info[star+data]) # 加入list2
                    # 加在后面的属性：比赛编号，team，红蓝方，获胜情况

                player.append(self.num)  #加入比赛序号
                if is_chinese(info[team+'_name']):
                    return 0
                else:
                    player.append(info[team+'_name'])  #加入战队名
                player.append(weizhi) #比赛位置
                player.append(team) #比赛持方
                player.append(str(info['game_time_m']+info['game_time_s'])) #比赛时间
                player.append(info[team+'_result']) #获胜情况
                players.append(player)
                player=[]

        return  players


def is_chinese(string):
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True

    return False


