from django.urls import path
from .views import home,login,cards,posts,logout

urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
     path('cards/',cards,name='cards'),
      path('posts/',posts,name='posts'),
      path('logout/',logout,name='logout'),
]
