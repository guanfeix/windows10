from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class ClassifyInfo(models.Model):
    title = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    # 1.最好一个魔法方法来说明
    #2.id或者说主键可定义，也可以不做系统会自动创建，若想自己创建需添加PK属性
    def __str__(self):
        return self.title


class GoodsInfo(models.Model):
    title = models.CharField(max_length=20)
    pic = models.ImageField(upload_to="media")
    price = models.DecimalField(max_digits=6,decimal_places=2,default=12.23,)
    isDelete = models.BooleanField(default=False)
    unit = models.CharField(max_length=20,default="500g")
    popularity = models.IntegerField(default=12,auto_created=True)
    sales = models.IntegerField(default=50,auto_created=True)
    stocks = models.IntegerField(default=500)
    profile = models.CharField(max_length=200,default="delicious")
    description = HTMLField(max_length=5000,default="delicious")
    comment = models.TextField(default="delicious")
    classify = models.ForeignKey(ClassifyInfo,on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    recommend = models.BooleanField(default=False)

    def __str__(self):
        return self.title