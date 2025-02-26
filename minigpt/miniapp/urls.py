from django.urls import path
from . import views

urlpatterns = [

    #Common
    path('', views.register_view, name='register'),
    path('index/', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    #User
    path('get-response/', views.chat_response, name='chat_response'),
    path('get-chat-history/', views.get_chat_history, name='get_chat_history'),

    #Admin
    path('adminDashboard/', views.admin_dashboard_view, name='adminDashboard'),
    path('adminDashboard/users/', views.view_all_users, name='viewAllUsers'),
    path('adminDashboard/users/update/<int:user_id>/', views.update_user, name='updateUser'),
    path('adminDashboard/users/delete/<int:user_id>/', views.delete_user, name='deleteUser'),
]
