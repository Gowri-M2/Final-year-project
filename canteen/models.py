from django.db import models
from django.db.models import Sum
from django.db.models import F
# Create your models here.

class canteen_details(models.Model):
    canteen_name=models.CharField(max_length=200)
    cmail_id=models.CharField(max_length=200)
    ccontact_no=models.CharField(max_length=12)
    caddress=models.CharField(max_length=200)
    clocation=models.CharField(max_length=200)
    def _str_(self) :
        return self.canteen_name

class user_details(models.Model):
    user_fullname=models.CharField(max_length=200)
    user_emailid=models.CharField(max_length=200)
    user_contactnumber=models.CharField(max_length=200)
    pwd=models.CharField(max_length=200,default="")

class food_details(models.Model):
    canteen_id=models.ForeignKey(canteen_details,on_delete=models.CASCADE)
    food_name=models.CharField(max_length=200)
    food_rate=models.IntegerField(max_length=200)
    food_image=models.ImageField(upload_to='images/', default="")
    def _str_(self) :
        return self.food_name

class ctransaction(models.Model):
    food_quantity=models.IntegerField(max_length=200)
    date=models.DateField()
    canteen_id=models.ForeignKey(canteen_details,on_delete=models.CASCADE)
    food_id=models.ForeignKey(food_details,on_delete=models.CASCADE)
    total=models.DecimalField(max_digits=10, decimal_places=2)
    

    @property
    def food_rate(self):
        return self.food_id.food_rate
    
    


class food_menu(models.Model):
    date=models.CharField(max_length=200)
    canteen_id=models.ForeignKey(canteen_details,on_delete=models.CASCADE)
    food_id=models.ForeignKey(food_details,on_delete=models.CASCADE)
    @property
    def food_image(self):
        return self.canteen_id.food_image
    @property
    def food_rate(self):
        return self.canteen_id.food_rate

