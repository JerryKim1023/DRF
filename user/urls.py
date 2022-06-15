from django.urls import path
from . import views

urlpatterns = [
	path('', views.UserApiView.as_view(), name="user_api_view"), # signup, login 등 user의 기본적인 api담당
	path('view/', views.UserView.as_view(), name="user_view"), # 같은 취미의 users를 찾는 등 추가기능 담당
	path('list/', views.ListUsers.as_view(), name="login_user_view"),
]
