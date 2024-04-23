# 本文件用来存放数据结构
# 1.距离表//
# 2.可用车辆栈//
# 3.新订单栈 //
# 4.运营车辆 //
from . import API
from itertools import permutations


# 订单栈
class NewOrder(object):
    date = "-"  # 类属性
    sum = 0
    tag = 0

    def __init__(self, date, command):  # 构建订单时传入日期
        if command == 'create':
            self.date = date
            self.tag = 1
            self.NOList = []
            print("Successful creating OrderList!")
        else:
            print("error!")

    def GetSize(self):
        return len(self.NOList)

    # 加一个返回订单信息的函数 order是一个列表 [编号 [起点经纬度 终点经纬度]] number从0开始
    def GetOrder(self, number):
        if number < len(self.NOList):
            return self.NOList[number]
        else:
            return -1

    def SearchOrder(self, order):  # 本方法用来查询指定订单在新订单栈中的下标(从0开始)
        i = 0  # order -> oid,position
        for n in self.NOList:
            if n == order:
                return i
            i += 1
        return -1  # 返回-1说明该订单不存在

    def AddOrders(self, order):  # 本方法用来更新订单,返回序号，不是返回下标
        self.NOList.append(order)
        self.sum += 1
        return self.sum

    def DeleteOrder(self, tag):
        print(f"删掉了{tag}", self.NOList[tag - 1])
        self.sum -= 1
        del self.NOList[tag - 1]

    def PopOrders(self, number):  # 本方法用来删除订单
        for nol in self.NOList:
            if nol[0] == number:
                self.NOList.remove(nol)
                self.sum -= 1
                return True
        return False

    def Show(self):
        print(self.NOList)
        print(self.sum)
        print(self.tag)
        print(self.date)


# 可用车辆栈
class AvailableVehicle(object):

    def __init__(self, command):  # 构建时传入日期
        if command == 'create':
            self.VList = []
            self.sum = 0
            print("Successful creating AvailableVehicleList!")
        else:
            print("error!")

    def GetSize(self):
        return len(self.VList)

    def SearchVehicle(self, VehicleID):  # 本方法用来查询指定订单在新订单栈中的下标(从0开始)
        i = 0
        for n in self.VList:
            if n[0] == VehicleID:
                return i
            i += 1
        return -1  # 返回-1说明该车辆不存在

    def AddVehicle(self, VehicleID):  # 本方法用来添加新空余车辆信息
        # Position转化函数，确定其位于哪个格子里
        self.VList.append(VehicleID)
        self.sum += 1

    def PopVehicle(self, VehicleID):  # 本方法用来删减空闲车辆信息
        for v in self.VList:
            if v == VehicleID:
                self.VList.remove(v)
                self.sum -= 1
        return

    def Show(self):
        print(self.VList)
        print(self.sum)


class UnavailableVehicle(object):

    def __init__(self, command):  # 构建栈
        if command == 'create':
            self.sum = 0
            self.UList = []
            print("Successful creating UnavailableVehicleList!")
        else:
            print("error!")

    def SearchVehicle(self, VehicleID):  # 本方法用来查询指定订单在新订单栈中的下标(从0开始)
        i = 0
        for n in self.UList:
            if n[0] == VehicleID:
                return i
            i += 1
        return -1  # 返回-1说明该车辆不存在

    def AddVehicle(self, ac: AvailableVehicle):
        if ac.GetSize() > 0:
            v = ac.VList[ac.GetSize()-1]
            self.UList.append(v)
            ac.PopVehicle(v)
            return True
        else:
            return False

    def PopVehicle(self, VehicleID, ac: AvailableVehicle):  # 本方法用来删除运营车辆
        i = 0
        for u in self.UList:
            if u[0] is VehicleID:
                del self.UList[i]
                ac.AddVehicle(VehicleID)
                break
            i += 1
        self.sum -= 1

    def Show(self):
        print(self.UList)
        print(self.sum)


class Distance(object):  # 距离表

    def __init__(self, date, command):
        if command == "create":
            self.date = date
            self.DList = []
            self.size = 0  # 规模
            print("Successfully creating DistanceList!")
        else:
            print("error!")

    def ShowDL(self):
        print(self.size)
        print(self.DList)

    def AddOrder(self, NewPosition, no):  # NewPosition只有一组数据，OldPosition有多组数据(下标从0开始)
        OldPosition = []
        if no:
            for j in range(no.GetSize()):
                OldPosition.append(no.GetOrder(j)[1])
        if self.size == 0:
            self.size += 1
            # print("AddOrder successfully!")
            return
        elif self.size > 0:
            print("插入第" + str(self.size + 1) + "个上车点")
            n = self.size  # 应插入的数据量
            k = n
            for i in range(n):
                if i == 0:
                    # print(NewPosition)
                    # print("==================================================================================")
                    self.DList.insert(0, API.get_distance(NewPosition[1] + ',' + NewPosition[0],
                                                          OldPosition[0][1] + ',' + OldPosition[0][0]))
                else:
                    # print(NewPosition[1] + ',' + NewPosition[0])
                    # print(OldPosition[i][1] + ',' + OldPosition[i][0])
                    self.DList.insert(k, API.get_distance(NewPosition[1] + ',' + NewPosition[0],
                                                          OldPosition[i][1] + ',' + OldPosition[i][0]))
                    k += (n - i)
            # print("AddOrder successfully!")
            self.size += 1
        else:
            print("error!")

    def DeleteOrder(self, k):  # 删除订单池中第k个订单的数据,k从1开始
        n = self.size
        if k > n:
            print("error!")
        elif k == 1:
            for i in range(n - 1):
                del self.DList[0]
        else:
            d = n - k
            print("现在规模为:", n)
            print("要删除：", k)
            for i in range(k - 1):
                print("现在删:", d)
                del self.DList[d]
                d += (n - i - 2)
            d -= 2
            #########################################################################
            for i in range(n - k):
                print("现在删:", d)
                print(len(self.DList))
                del self.DList[d]
                print("成功")
        self.size -= 1

    def GetDistance(self, start, end):  # 传进来两个订单池编号（从1开始）
        if start > end:
            tmp = start
            start = end
            end = tmp
        elif start == end:
            return -1
        n = 0
        for i in range(start - 1):
            n += (self.size - i - 1)
        n += (self.size - end)
        # print(n)
        return self.DList[n]

    def GetStartPos(self, OrderStack: NewOrder):  # OrderStack是一个订单栈对象,返回值是列表
        n = self.size
        if n >= 1:
            # 先找到起点
            m = 0
            pos = 0
            j = 0
            for d in self.DList:
                if float(d) > m:
                    m = float(d)
                    pos = j
                j += 1
            # 下标从0开始
            for i in range(n - 1):
                pos -= (n - 1 - i)
                if pos < 0:
                    column = pos + (n - 1 - i)
                    E = OrderStack.GetOrder(n - column - 1)[1]
                    S = OrderStack.GetOrder(i)[1]
                    if float(S[0]) < float(E[0]):
                        return [S, i + 1]  # 返回的是从1开始的
                    else:
                        return [E, n - column]
        else:
            return ["NoAnswer!"]

    def Final(self, c: list):
        m = 100000
        D = []
        for num in permutations(c, len(c)):
            a = []
            s = 0
            for i in range(len(c)):
                a.append(num[i])
                if i > 0:
                    s += float(self.GetDistance(num[i - 1], num[i]))

            if s < m:
                m = s
                D = []
                for j in range(len(a)):
                    D.append(a[j])
        if m == 10000:
            m = 0
        return D, m

    def Classify(self, OrderStack: NewOrder):
        classify = []
        while self.size > 0:
            n = self.size
            print("======================", n)
            b = []
            c = []  # 乘车表
            S = self.GetStartPos(OrderStack)  # 起点
            print("起点是", S)
            c.append(S[1])
            b.append(OrderStack.GetOrder(S[1] - 1))
            All = []
            if n >= 5:
                # print("n=", n)
                for j in range(5):
                    # print("j=", j)
                    pos = 0
                    m = 100000
                    if j == 4:
                        break
                    for i in range(n):
                        if j == 0:  # 确定了起点就对All表初始化
                            # print("j=", j)
                            if (i + 1) != S[1]:
                                All.append(self.GetDistance(S[1], i + 1))
                                if float(self.GetDistance(S[1], i + 1)) < float(m):
                                    pos = i + 1
                                    m = float(All[i])
                            else:
                                All.append(0)
                        else:
                            if (i + 1) not in c:
                                if self.GetDistance(c[j], i + 1) + self.GetDistance(c[0], c[j]) < All[i]:
                                    All[i] = self.GetDistance(c[j], i + 1) + self.GetDistance(c[0], c[j])
                                if float(All[i]) < float(m):
                                    # 特别注意，这里要转成绝对订单编号
                                    pos = i + 1
                                    m = All[i]
                    c.append(pos)
                    b.append(OrderStack.GetOrder(pos - 1))
                    count = 0
                    for C in c:
                        print(C)
                        if C < pos:
                            count += 1
                    print("已分组:", c)
                classify.append([])
                # 深层次拷贝
                dic = dict()
                for i in range(5):
                    dic[c[i]] = b[i]
                c, minDis = self.Final(c)
                for i in range(5):
                    classify[len(classify) - 1].append(dic[c[i]])
                # classify[len(classify) - 1].append(False)  # 这个布尔值用来标记还未派车
                print("b:", classify)
                print("现在规模为：", self.size)
                print("===============================")
                print("c:", c)
                last = self.size + 2
                for i in range(5):
                    for k in range(5):
                        if c[k] > last:
                            c[k] -= 1
                    last = c[i]
                    print(last)
                    print("现在距离表是这样的：")
                    self.DeleteOrder(last)  # 这里是删除距离表中的订单数据
                    OrderStack.DeleteOrder(last)
                print("现在规模为：", self.size)
            else:
                print("最后一组：", n)
                for j in range(n):
                    pos = 0
                    m = 100000
                    if j == n - 1:
                        break
                    for i in range(n):
                        if j == 0:  # 确定了起点就对All表初始化
                            if (i + 1) != S[1]:
                                All.append(self.GetDistance(S[1], i + 1))
                                if self.GetDistance(S[1], i + 1) < m:
                                    pos = i + 1
                                    m = All[i]
                            else:
                                All.append(0)
                        else:
                            if (i + 1) not in c:
                                if self.GetDistance(c[j], i + 1) + self.GetDistance(c[0], c[j]) < All[i]:
                                    # print("替换到" + str(i + 1))
                                    All[i] = self.GetDistance(c[j], i + 1) + self.GetDistance(c[0], c[j])
                                if All[i] < m:
                                    pos = i + 1
                                    m = All[i]
                                    # print(All)
                                    # print("pos=", pos)
                    c.append(pos)
                    b.append(OrderStack.GetOrder(pos - 1))
                    count = 0
                    for C in c:
                        if C < pos:
                            count += 1
                    if OrderStack != '':
                        OrderStack.PopOrders(OrderStack.GetOrder(pos - count))
                    print("已分组:", c)
                classify.append([])
                # 深层次拷贝
                dic = dict()
                print(b)
                OrderStack.Show()
                print("======================================")
                for i in range(n):
                    print("现在到：", i)
                    dic[c[i]] = b[i]

                c, minDis = self.Final(c)
                for i in range(n):
                    classify[len(classify) - 1].append(dic[c[i]])
                # classify[len(classify) - 1].append(False)  # 这个布尔值用来标记还未派车
                print("b:", classify)
                print("现在规模为：", self.size)
                self.ShowDL()
                OrderStack.Show()
                # print("===============================")
                print("c:", c)
                last = n + 1
                for i in range(n):
                    for k in range(n):
                        if c[k] > last:
                            c[k] -= 1
                    last = c[i]
                    print(last)
                    self.DeleteOrder(last)  # 这里是删除距离表中的订单数据
                    OrderStack.DeleteOrder(last)
                self.ShowDL()
                OrderStack.Show()
                # print("现在规模为：", self.size)

        return classify

    def Change(self):
        for i in range(len(self.DList)):
            self.DList[i] = float(self.DList[i])


if __name__ == '__main__':
    # 首先传入7个订单
    DS = Distance("2023-4-23", "create")
    '''DS.T(['3455', '3030', '4892', '12812', '4299', '3658', '6037', '5494', '8881', '3107', '33417', '18522', '2356',
          '2534', '3169', '6000', '15480', '3909', '3797', '7145', '6698', '9989', '2452', '34525', '19630', '18643',
          '16499', '14694', '8083', '18044', '16830', '14083', '17335', '11774', '15333', '15300', '31031', '28887',
          '27082', '20471', '30432', '29218', '26471', '29723', '24162', '27721', '4379', '1989', '3893', '13373',
          '3258', '2617', '3559', '4460', '7546', '10567', '5900', '4336', '8506', '5441', '6231', '3725', '5175',
          '6313', '2731', '4056', '13536', '991', '1977', '3261', '8593', '3926', '2362', '11058', '4084', '4257',
          '4337', '5634', '7249', '16729', '3112', '5823', '3903', '5228', '14708', '12972', '8305', '6662', '8761',
          '5615', '6398']
         )'''
    DS.ShowDL()
    print(DS.Classify(''))
