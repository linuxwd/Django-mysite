cd c:\Users\Administrator\Desktop\Django版餐厅管理系统\Django-mysite\mysite\
c:\Python35\python.exe c:\Users\Administrator\Desktop\Django版餐厅管理系统\Django-mysite\mysite\manage.py shell
from restaurants.models import Restaurant,Food
restaurants = Restaurant.objects.all()
restaurants
quit()