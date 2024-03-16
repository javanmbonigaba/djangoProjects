from django.urls import path
from .views import *

urlpatterns = [
    #path('', home, name='home'),
    path('', index),
    path('buyer/', buyer, name='buyers'),
    path('login/', loginuser, name='login'),
    path('user_logout/', user_logout, name='logout'),

]