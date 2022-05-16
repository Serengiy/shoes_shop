from django.urls import path
from users.views import registration_view

app_name = 'accounts'

urlpatterns = [
    path('register/', registration_view, name='register'),
]