'''
本文件用于英雄联盟赛事数据爬取测试
本文件作用于score
本文件在此详细分析
'''

# -------------------代码区域--------------------------------------#
import requests
import json

def get_info(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}
    response = requests.get(url=url,headers=headers)
    return response.text
#lpl夏季赛从32216开始，到34142截至
info_team = get_info('https://img.scoregg.com/match/result/32225.json?_=1660730052072')
info = json.loads(info_team)['data']  # 将str对象转换为dict（字典）对象
#print(info)
'''
对文件分析：
基础信息：



'''
# 比赛中最大数据   今日赛果
print('日期',info['updated_at'])
print('总mvp',info['max_mvp'])
print('背锅侠',info['max_beiguo'])
print('最多钱',info['max_money'])
print('最多击杀',info['max_kills'])
print('最多助攻',info['max_assists'])
print('最多死亡',info['max_deaths'])
print('最高伤害',info['max_damage_dealt'])
print('最高承伤',info['max_damage_taken'])
print('最高连杀',info['max_hits'])

info=info['result_list'] #最终结果
print("红方名字",info['red_name'])
print('游戏时间',info['game_time_m'],info['game_time_s'])
print('红方胜败',info['red_result'])
print('红方小龙',info['red_small_dargon'])
print('红方大龙',info['red_big_dargon'])
print('红方推塔',info['red_tower'])
print('红方击杀',info['red_kill'])
print('红方死亡',info['red_die'])
print('红方助攻',info['red_asses'])
print('红方经济',info['red_money'])

#选手情况 命名方法  red_star_a   red_star_b red_star_c red_star_d red_star_e
print('红方选手1 kda kills deaths assists:',info['red_star_a_name'],info['red_star_a_kda'],info['red_star_a_kills'],info['red_star_a_deaths'],info['red_star_a_assists'])
print('红方选手2 kda kills deaths assists:',info['red_star_b_name'],info['red_star_b_kda'],info['red_star_b_kills'],info['red_star_b_deaths'],info['red_star_b_assists'])
print('红方选手3 kda kills deaths assists:',info['red_star_c_name'],info['red_star_c_kda'],info['red_star_c_kills'],info['red_star_c_deaths'],info['red_star_c_assists'])
print('红方选手4 kda kills deaths assists:',info['red_star_d_name'],info['red_star_d_kda'],info['red_star_d_kills'],info['red_star_d_deaths'],info['red_star_d_assists'])
print('红方选手5 kda kills deaths assists:',info['red_star_e_name'],info['red_star_e_kda'],info['red_star_e_kills'],info['red_star_e_deaths'],info['red_star_e_assists'])
print("参团率",info['red_star_a_part'])
'''
red_star_a_atk  输出 按k记录
red_star_a_atk_o 输出 按数字记录
red_star_a_atk_p 输出 按占比记录
red_star_a_atk_m 输出 分均

red_star_a_def  承伤 按k记录
red_star_a_def_o 承伤 按数字记录
red_star_a_def_p 承伤 按比例记录
red_star_a_atk_m 承伤 分均

red_star_a_adc_m 分均补刀

red_star_a_money 总经济 按k记录
red_star_a_money_o 总经济 按数字记录
red_star_a_money_M 分均经济

red_a_skill_1 召唤师技能1图标
red_a_skill_2 召唤师技能2图标
red_star_a_equip_1 装备栏1图标
red_star_a_equip_7 装备栏1图标

red_star_a_wp_m  每分钟安置视野数
red_star_e_hits   补兵
red_hero_b_name  选择英雄
'''
