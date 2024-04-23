import os
from io import BytesIO

import requests
import json
import datetime
import math

from PIL import Image

'''
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code:{r.status_code}')
response_dict = r.json()
print(response_dict.keys())'''

url = 'https://restapi.amap.com/v3/direction/driving?parameters'


def NewMap():
    key = '655f81557f1f3a4b62255505872f849d'
    api = f"https://restapi.amap.com/v3/staticmap?location=116.481485,39.990464&zoom=10&size=750*300&markers=mid,,A:116.481485,39.990464&key={key}"
    r = requests.get(api)
    print(r.url)


# 里程计算
def get_distance(origin, destination):
    key = '655f81557f1f3a4b62255505872f849d'
    api = f'https://restapi.amap.com/v3/direction/driving?origin={origin}&destination={destination}&strategy=1&extensions=all&output=json&key={key}'
    r = requests.get(api)
    jsonData = r.json()
    return jsonData['route']['paths'][0]['distance']


# 这个函数直接返回两点之间的距离在位置表中的下标
def search(C, N_Origin, N_Destination):  # C是总长度 N_Origin起点编号，N_Destination终点编号
    if N_Origin == N_Destination:
        return "瞎搞什么，起点和终点一样辣！"
    elif N_Origin < N_Destination:  # 交换起止点编号,成为标准格式
        tmp = N_Origin
        N_Origin = N_Destination
        N_Destination = tmp
    # 确定一下在表中方位
    COLUMN = C - N_Origin + 1
    ROW = N_Destination
    TAG = -1
    for i in range(ROW - 1):
        TAG += (C - i)
    TAG += COLUMN
    TAG -= (ROW - 1)
    return TAG


# 这个函数直接跟据位置表中的下标返回两个点的编号(从1开始)
def lock(C, TAG):
    l = len(C)
    total = (math.sqrt(l * 8 + 1) + 1) / 2
    n = int(total)
    start_pos = 0
    while TAG > 0:
        # print(TAG)
        start_pos += 1
        # print(start_pos)
        n -= 1
        TAG -= n
    TAG += n
    end_pos = int(total - TAG + 1)
    return start_pos, end_pos, int(total)





if __name__ == '__main__':
    '''print(get_distance("118.084453,24.468734", "118.080484,24.642523"))
    format = '%Y-%m-%d %H:%M:%S'
    a = datetime.datetime.strptime('2023-02-03 12:00:01', format)
    b = datetime.datetime.strptime('2023-02-03 12:00:00', format)
    print(a)
    print(b)
    print(a > b)
    s = [100, 12, 9, 8, 1, 20, 10, 9, 1, 5, 7, 1, 19, 1, 1]
    print(s)
    b, c, d = lock(s, 1)
    print(b)
    print(c)'''
    print(1)
    #                   ['118.043463886,24.560544313', '118.152732052,24.497479139', '118.183829627,24.485377074',
    #                      '118.103459046,24.494203184', '118.13010548769,24.434124208528']
