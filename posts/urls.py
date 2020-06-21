from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('send/',views.send,name = 'send'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('singup/', views.singup, name= 'singup'),
    path('singup/saveuser/', views.saveuser, name= 'saveuser'),
    path('test/', views.test,name='test'),
    path('products/', views.shop,name='shop'),
    path('products/<int:shop_id>',views.shop_buy,name='shop_buy'),
    path('products/landing/<int:shop_id>',views.curselanding,name='landing '),
    path('profile/', views.profile,name='profile'),
    path('profile/<int:curse_id>',views.current_curse,name='current_curse'),
    path('profile/<int:curse_id>/<int:les_id>',views.current_lesson,name='current_lesson'),
    path('profile/<int:curse_id>/<int:les_id>/leavecomment',views.new_comm,name='new_comm'),
    path('profile/<int:curse_id>/<int:les_id>/<int:com_id>/leavereply',views.new_reply,name='new_reply')
]


