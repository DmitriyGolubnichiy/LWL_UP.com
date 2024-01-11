from django.urls import path

from users.views import log_in,register,profile,logout

app_name = 'users'

urlpatterns = [
    path("log_in/", log_in ,name='log_in' ),
    path('register/',register, name='register'),
    path('profile/',profile,name='profile'),
    path('logout/',logout,name='logout'),
]