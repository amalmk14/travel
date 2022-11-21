from .  import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    # path('',views.math,name='math'),
    # path('result/',views.ans,name='ans'),
    # path('hello/',views.hello,name='hello')
]
