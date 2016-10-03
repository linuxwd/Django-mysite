c:\Python35\python.exe c:\Users\Administrator\Desktop\Django版餐厅管理系统\Django-mysite\mysite\manage.py shell
from django import template
t = template.Template('I love {{ name }}.')
c = template.Context({ 'name':'Mary' })
print(t.render(c))
