from django.urls import path
from main.views import home, contact, admin, delete_user

urlpatterns=[
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('admin_page/', admin, name='admin_page'),
    path('delete_user/', delete_user, name='delete_user'),
]