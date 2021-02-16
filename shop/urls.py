from django.urls import path

import shop.views as v

urlpatterns = [
    path('', v.view_dishes, name='index'),


]