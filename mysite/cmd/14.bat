cd c:\Users\Administrator\Desktop\Django版餐厅管理系统\Django-mysite\mysite\
c:\Python35\python.exe c:\Users\Administrator\Desktop\Django版餐厅管理系统\Django-mysite\mysite\manage.py shell
from restaurants.models import Restaurant,Food
restaurants = Restaurant.objects.filter(name='古意得餐厅',phone_number='02-7654321')
restaurants
quit()

