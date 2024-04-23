from django.http import HttpResponse

from Model.models import Data

# 数据库操作
def testdb(request):


    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Data.objects.all().values('passengerid')

   # print(response3)  response3 = Data.objects.get(passengerid='1')
    return HttpResponse(list)

