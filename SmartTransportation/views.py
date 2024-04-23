import datetime
from io import BytesIO

import requests
import os

import pymysql
from PIL import Image
from django.http import HttpResponse
from django.shortcuts import render
from Model.models import Data, Reservation, Car
from django.db.models import Q
from SmartTransportation import map

from . import SC
from .login import check_login

# date = datetime.date.today()
# print(date)

date = "2023-02-01"
pointer = 0  # 现在取到第几个订单了
orders = SC.NewOrder("2023-02-01", "create")
car = SC.AvailableVehicle("create")
Ucar = SC.UnavailableVehicle("create")
Ovc = Car.objects.all()
Ova = Reservation.objects.all()  # 从数据库读取订单
last = pointer
distance = SC.Distance("2023-02-01", "create")
n = 0
con = []


# @check_login
def login(request):
    return render(request, 'login.html')  # 打开登录界面


def login2(request):
    return render(request, 'login2.html')  # 打开登录界面


def add(request):
    return render(request, 'add.html')


def delete(request):
    return render(request, 'delete.html')


def edit(request):
    return render(request, 'edit.html')


def search(request):
    return render(request, 'search.html')


al = []


def adds(request):
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='smart transportation')
    cursor = db.cursor()
    cursor.callproc("into_supplyrecord", (al[0], request.GET.get(k + '货物编号'), request.GET.get(k + '货物数量')))
    db.commit()
    return render(request, 'add.html')


def delete1(request):
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='smart transportation')
    cursor = db.cursor()
    selection = request.GET['selection']
    No = request.GET['q']
    if selection == "customer":
        obj = passenger.objects.get(PassengerID=No)
        obj.delete()
    elif selection == "warehouse":
        obj = driver.objects.get(DriverID=No)
        obj.delete()
    elif selection == "goods":
        obj = car.objects.get(CarID=No)
        obj.delete()
    elif selection == "supplier":
        obj = order.objects.get(OrderID=No)
        obj.delete()
    db.commit()
    return render(request, 'delete.html')


def edit2(request):
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='smart transportation')
    cursor = db.cursor()
    cursor.callproc("into_supplyrecord", (al[0], request.GET.get(k + '货物编号'), request.GET.get(k + '货物数量')))
    db.commit()
    return render(request, 'edit.html')


def select(request):
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='Warehouse')
    cursor = db.cursor()
    selection = request.GET['selection']
    if selection == "W_id":
        cursor.callproc("wid1", (request.GET['q'],))  # 参数为存储过程名称和存储过程接收的参数
    elif selection == "W_location":
        cursor.callproc("wlocation1", (request.GET['q'],))  # 参数为存储过程名称和存储过程接收的参数

    db.commit()
    # 获取数据
    data = cursor.fetchall()
    if data == ():
        data = None
    param_value = cursor.fetchone()
    # 关闭数据库连接
    db.close()
    return render(request, "WarehouseMessage.html", {"data": data})  # 打开搜索货物界面


def mainpage(request):
    print(Data.objects.all())
    return render(request, "mainpage.html")


def manager(request):
    return render(request, "manager.html")


def p2(request):
    if request.method == 'POST':
        num1 = request.POST.get('num1', 0)

        if num1 == '6':
            num = '/static/img/prediction/p6.jpg'
            return HttpResponse(str(num))  # POST请求仅返回HttpResponse值
        if num1 == '8':
            num = '/static/img/prediction/p8.jpg'
            return HttpResponse(str(num))
        if num1 == '10':
            num = '/static/img/prediction/p10.jpg'
            return HttpResponse(str(num))
        if num1 == '12':
            num = '/static/img/prediction/p12.jpg'
            return HttpResponse(str(num))
        if num1 == '14':
            num = '/static/img/prediction/p14.jpg'
            return HttpResponse(str(num))
        if num1 == '16':
            num = '/static/img/prediction/p16.jpg'
            return HttpResponse(str(num))
        if num1 == '18':
            num = '/static/img/prediction/p18.jpg'
            return HttpResponse(str(num))
        if num1 == '20':
            num = '/static/img/prediction/p20.jpg'
            return HttpResponse(str(num))
        else:
            num = '/static/img/prediction/map.png'
            return HttpResponse(str(num))

    # GET请求返回error.html界面
    return render(request, "page2.html")


def CreateMap(startpoint: list, number: int, Day: str):
    '''
    https://restapi.amap.com/v3/staticmap?location=116.481485,39.990464&
    zoom=10&size=750*300&markers=mid,,A:116.481485,39.990464&key=<用户的key>
    '''
    m = startpoint[0]
    url = 'https://restapi.amap.com/v3/staticmap'
    p = '10,0x0000ff,1,,:'
    l = len(startpoint)
    for s in startpoint:
        p += s
        if s != startpoint[l - 1]:
            p += ';'
    print(p)
    params = {
        'size': '1024*1024',
        'traffic': '1',
        'markers': 'mid,,S:' + m,
        'paths': p,
        'key': '655f81557f1f3a4b62255505872f849d'
    }
    path = os.getcwd()
    n = len(path)
    new_path = ''
    for i in range(n):
        if i < n - 6:
            new_path = new_path + path[i]
    r = requests.get(url, params=params)
    new_path = os.path.relpath(r"C:\Users\86133\Desktop\23camp\test1\static\img\manage")
    print(new_path)
    # 将bytes结果转化为字节流
    bytes_stream = BytesIO(r.content)
    # 读取到图片
    roiimg = Image.open(bytes_stream)
    #roiimg.show()
    roiimg.save('static\\img\\manage' + '\\' + Day + '_' + str(number) + '.png')
    return roiimg


def p1(request):
    global date
    if request.method == 'POST':
        num1 = request.POST.get('d1', 0)
        str(num1)
        num = '/static/img/manage/'+date+'_'+num1+'.png'
        return HttpResponse(str(num))  # POST请求仅返回HttpResponse值
    views_list = Reservation.objects.all()
    global Ova
    global orders
    global pointer
    global last
    global distance
    global n
    global con
    for c in Ovc:
        if c.carstate == 1:
            car.AddVehicle(c.carid)
    if pointer < len(Ova):
        pointer += 20
    i = 0
    # print(Ova[i].startinglongitude, Ova[i].startinglatitude)
    for j in range(last, pointer):
        if i == 0:
            distance.AddOrder([Ova[j].startinglongitude, Ova[j].startinglatitude], [])
        else:
            # print("i=", i)
            # print("============================")
            distance.AddOrder([Ova[j].startinglongitude, Ova[j].startinglatitude], orders)
            # distance.ShowDL()
        orders.AddOrders([Ova[j].reservationid, [Ova[j].startinglongitude, Ova[j].startinglatitude]])
        # print("-------------------------------------")
        # orders.Show()
        i += 1
    orders.Show()
    distance.Change()
    distance.ShowDL()
    result_list = distance.Classify(orders)
    RL = []
    for i in result_list:
        # 出发点位置打包
        n += 1
        RL.append([])
        package = []
        for j in i:
            RL[len(RL) - 1].append(j[0] + " 第" + str(n) + '组')
            package.append(j[1][1] + ',' + j[1][0])
        print(package)
        CreateMap(package, n, date)
    # 安排车辆
    con += RL
    POST = []
    '''
    for i in range(car.GetSize()):
        if i >= len(con):
            break
        POST += con[i]
        car.PopVehicle(car.VList[i])
        Car.objects.filter(carid=car.VList[i]).update(carstate=2)
        con.pop(i)
    print("POST:", POST)'''
    return render(request, "page1.html", {"views_list": views_list, "result_list": RL})


# Create your views here.
def web_show(request):
    x_list = ['周一', '周三', '周四', '周五', '周六', '周日']
    y_list = [
        Data.objects.filter(reservationtime__contains='2023-02-06').count(),
        Data.objects.filter(reservationtime__contains='2023-02-01').count(),
        Data.objects.filter(reservationtime__contains='2023-02-02').count(),
        Data.objects.filter(reservationtime__contains='2023-02-03').count(),
        Data.objects.filter(reservationtime__contains='2023-02-04').count(),
        Data.objects.filter(reservationtime__contains='2023-02-05').count(),
    ]
    day_list = [
        Data.objects.filter(Q(reservationtime__contains='2023-02-06') | Q(dispatchtime__lt='2023-02-06 17:00')).count(),
        Data.objects.filter(Q(reservationtime__contains='2023-02-01') | Q(dispatchtime__lt='2023-02-01 17:00')).count(),
        Data.objects.filter(Q(reservationtime__contains='2023-02-02') | Q(dispatchtime__lt='2023-02-02 17:00')).count(),
        Data.objects.filter(Q(reservationtime__contains='2023-02-03') | Q(dispatchtime__lt='2023-02-03 17:00')).count(),
        Data.objects.filter(Q(reservationtime__contains='2023-02-04') | Q(dispatchtime__lt='2023-02-04 17:00')).count(),
        Data.objects.filter(Q(reservationtime__contains='2023-02-05') | Q(dispatchtime__lt='2023-02-05 17:00')).count(),
    ]
    night_list = [
        Data.objects.filter(
            Q(reservationtime__contains='2023-02-06') | Q(dispatchtime__gte='2023-02-06 17:00')).count(),
        Data.objects.filter(
            Q(reservationtime__contains='2023-02-01') | Q(dispatchtime__gte='2023-02-01 17:00')).count(),
        Data.objects.filter(
            Q(reservationtime__contains='2023-02-02') | Q(dispatchtime__gte='2023-02-02 17:00')).count(),
        Data.objects.filter(
            Q(reservationtime__contains='2023-02-03') | Q(dispatchtime__gte='2023-02-03 17:00')).count(),
        Data.objects.filter(
            Q(reservationtime__contains='2023-02-04') | Q(dispatchtime__gte='2023-02-04 17:00')).count(),
        Data.objects.filter(
            Q(reservationtime__contains='2023-02-05') | Q(dispatchtime__gte='2023-02-05 17:00')).count(),
    ]
    return render(request, "testecharts.html",
                  {'x_list': x_list, 'y_list': y_list, 'day_list': day_list, 'night_list': night_list})
