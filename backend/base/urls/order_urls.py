from django.urls import path,include
from base.views import order_views as views

urlpatterns = [
  path('add/',views.addOrderItems,name='order-add'),
  path('<str:pk>/',views.getOrderByID,name='user-order'),
  path('<str:pk>/pay/',views.updateOrderToPaid,name='user-order-pay')
]