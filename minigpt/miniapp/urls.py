from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_view, name='register'),
    path('index/', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('get-response/', views.chat_response, name='chat_response'),
    path('get-chat-history/', views.get_chat_history, name='get_chat_history'),
]
