from django.db import models

# Create your models here.
class OrderInfo(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    user = models.ForeignKey("df_user.UserInfo",on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    IsPay = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=8,decimal_places=2)
    address = models.CharField(max_length=150, default="")
#     真实支付，物流信息，支付类型
class OrderDetailInfo(models.Model):
    goods = models.ForeignKey("df_goods.GoodsInfo", on_delete=models.CASCADE)
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    count = models.IntegerField()
