from django.db import models
class Product(models.Model):
    Pid=models.IntegerField(primary_key=True)
    Pname=models.CharField(max_length=10)
    Pcost=models.DecimalField(max_digits=10,decimal_places=4)
    Pmfdt=models.DateField()
    Pexpdt=models.DateField()


# Create your models here.
