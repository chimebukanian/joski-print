from os import name
from django.urls import path
from . import views

app_name="joskiprint"

urlpatterns=[
    path('', views.index, name='index'),
    path('user', views.userDetails.as_view(), name='user'),
    path('order/', views.makeOrder.as_view(), name='order'),
    path('printoptions/', views.printOptions.as_view(), name='printoptions'),
    path('order/<int:pk>', views.orderSuccessful.as_view(), name='ordersuccess'),
    path('signup/', views.userCreateview.as_view(), name='usersignup'),
    path('about', views.about, name='about'),
    path('successful_orders/', views.orderSuccesses.as_view(), name='successes'),
    path('order_update/<int:pk>', views.OrderUpdate.as_view(), name='order-update'),
    path('order_delete/<int:pk>', views.OrderDelete.as_view(), name='order-delete'),
    ]