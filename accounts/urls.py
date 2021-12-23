from django.urls import path
from .views import Register, LoginUser, LogoutUser, AccountHome

app_name = 'accounts'

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('', AccountHome.as_view(), name='home'),
]
