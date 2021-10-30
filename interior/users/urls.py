from django.urls import path

# from users.views import login, register, profile, new_logout
from users.views import login, ProfileFormView, Logout,RegisterListView,privacy_policy

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', RegisterListView.as_view(), name='register'),
    path('profile/', ProfileFormView.as_view(), name='profile'),
    path('', Logout.as_view(), name='new_logout'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('verify/<str:email>/<str:activation_key>/', RegisterListView.verify, name='verify'),

]