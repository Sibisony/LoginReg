from django.urls import path
from accounts import views
urlpatterns=[
path('',views.home,name="home"),
path('register/',views.register,name="register"),
path('profile/',views.profile,name="profile"),
path('logout',views.logout_page,name="logout_page"),
]