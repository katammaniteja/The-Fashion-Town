from django.urls import path
from . import views

from store.controller import authview,cart

urlpatterns=[
    path('',views.home,name='home'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:slug>',views.collectionsView,name="collectionsview"),
    path('collections/<str:cate_slug>/<str:pro_slug>',views.productView,name="productView"),

    path('register/',authview.register,name='register'),
    path('login/',authview.loginpage,name='loginpage'),
    path('logout/',authview.logoutpage,name='logoutpage'),

    path('add-to-cart',cart.addtocart,name='addtocart'),
    path('cart',cart.viewcart,name='viewcart')
]