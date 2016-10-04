cd c:\Users\Administrator\Desktop\Django版餐厅管理系统\Django-mysite\mysite\
c:\Python35\python.exe c:\Users\Administrator\Desktop\Django版餐厅管理系统\Django-mysite\mysite\manage.py shell
from restaurants.models import Restaurant,Food
r1 = Restaurant(name='派森家常小馆',phone_number='02-12345678',address='天龙国天龙区天龙路1号')
r1
r1.save()
quit()
