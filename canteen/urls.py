from django.contrib import admin
from django.urls import path 
from .views import *
urlpatterns = [
    
    path('home/',home),
    path('userhome/',userhome),
    path('changepin/',changepin),
    path('changepin_chk/',changepin_chk),
    path('chome/',chome),
    path('canteen_form/',canteen_form),
    path('user_form/',user_form),
    path('food_form/',food_form),
    path('ctransaction_form/',ctransaction_form),
    path('food_menu_form/',food_menu_form),
    
    path('food_view/',food_view),
    
    path('food_del/<int:fview_id>',food_del),
    path('food_update/<int:fview_id>',food_update),
    path('food_edit/<int:fview_id>',food_edit),

    path('canteen_view/',canteen_view),
    path('canteen_del/<int:cview_id>',canteen_del),
    path('canteen_update/<int:cview_id>',canteen_update),
    path('canteen_edit/<int:cview_id>',canteen_edit),

    path('user_view/',user_view),
    path('user_del/<int:uview_id>',user_del),
    path('user_update/<int:uview_id>',user_update),
    path('user_edit/<int:uview_id>',user_edit),

    path('ctransaction_view_date/',ctransaction_view_date),
    path('ctransaction_view/',ctransaction_view),
    path('ctransaction_del/<int:tview_id>',ctransaction_del),
    path('ctransaction_update/<int:tview_id>',ctransaction_update),
    path('ctransaction_edit/<int:tview_id>',ctransaction_edit),


    path('fmenu_view/',fmenu_view),
     path('fmenu_view_user/<int:cid>',fmenu_view_user),
    path('fmenu_del/<int:mview_id>',fmenu_del),
    path('fmenu_update/<int:mview_id>',fmenu_update),
    path('fmenu_edit/<int:mview_id>',fmenu_edit)


    

    

]
