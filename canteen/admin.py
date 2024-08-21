from django.contrib import admin
from .models import *

# Register your models here.
class canteenadmin(admin.ModelAdmin):
    list_display=('id','canteen_name','cmail_id','ccontact_no','caddress','clocation')
admin.site.register(canteen_details,canteenadmin)

class useradmin(admin.ModelAdmin):
    list_display=('id','user_fullname','user_emailid','user_contactnumber')
admin.site.register(user_details,useradmin)

class foodadmin(admin.ModelAdmin):
    list_display=('id','food_name','food_rate','food_image','canteen_id')
admin.site.register(food_details,foodadmin)

class transcationadmin(admin.ModelAdmin):
    list_display=('id','food_quantity','date','canteen_id','food_id')
admin.site.register(ctransaction,transcationadmin)


class foodmenuadmin(admin.ModelAdmin):
    list_display=('id','date','date','canteen_id','food_id')
admin.site.register(food_menu,foodmenuadmin)



