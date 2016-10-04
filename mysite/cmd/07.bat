cd c:\Users\Administrator\Desktop\Django版餐厅管理系统\Django-mysite\mysite\
c:\Python35\python.exe c:\Users\Administrator\Desktop\Django版餐厅管理系统\Django-mysite\mysite\manage.py shell
from restaurants.models import Restaurant,Food
r2 = Restaurant.objects.create(name='古意得餐厅',phone_number='02-7654321',address='天龙国天龙区天龙路100号')
r2
quit()
