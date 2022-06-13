from django.urls import path
from . import views

urlpatterns = [
	path('', views.UserView.as_view(), name="user_view"),
	path('list/', views.ListUsers.as_view(), name="login_user_view"),
]
