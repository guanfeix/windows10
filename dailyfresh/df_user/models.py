from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    receiver = models.CharField(max_length=20,default="")
    uaddress = models.CharField(max_length=100,default="")
    postcode = models.CharField(max_length=6,default="")
    uphone = models.CharField(max_length=11,default="")#值有映射到db才需要迁移，defaulT和blank，是在python层面的操作，并不会映射到db
    def __str__(self):
        return self.uname