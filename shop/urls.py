from django.urls import path
from shop import views


urlpatterns = [
    path('', views.HomeView.as_view(), name="index"),
    path('category/', views.view_category, name="category"),
    path('login/', views.log_in, name="login"),
    path('registr/', views.register, name="registr"),
    path('logouts/', views.logouts , name='logouts'),
    path('edit/', views.edit_dish, name='edit'),
    path('cart/', views.CartView.as_view(), name='cart'),


]

