from django.db import models

# Create your models here.
class CartInfo(models.Model):
    goods = models.ForeignKey("df_goods.GoodsInfo",on_delete=models.CASCADE)
    master = models.ForeignKey("df_user.UserInfo",on_delete=models.CASCADE)
    count = models.IntegerField()
    # 2.__str__ returned non-string (type int)
    #1.__str__ returned non-string (type UserInfo) 这样懂了外键的含义吗将另一模型对象作为模型类属性
    def __str__(self):
        return self.master.uname

