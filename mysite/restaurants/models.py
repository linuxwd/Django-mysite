from django.db import models

# Create your models here.
from django.db import models
class Restaurant(models.Model):
    #列名name，字符型，最大长度20
    name = models.CharField(max_length=20)
    #列名phone_number，字符型，最大长度15
    phone_number = models.CharField(max_length=15)
    #列名address，字符型，最大长度50，允许该字段为空（blank）
    address = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.name

class Food(models.Model):
    #列名name，字符型，最大长度20
    name = models.CharField(max_length=20)
    #列名price，浮点型，max_digits表示数字允许的最大位数（包括小数），decimal_places表示小数字数为2位小数
    price = models.DecimalField(max_digits=5,decimal_places=2)
    # 列名comment，字符型，最大长度50，blank=True表示该字段允许位空值
    comment = models.CharField(max_length=50,blank=True)
    #列名is_spicy，布尔型，默认值为false
    is_spicy = models.BooleanField(default=False)
    #列名restaurant，外键只想Restaurant表
    restaurant = models.ForeignKey(Restaurant)

    def __str__(self):
        return self.name