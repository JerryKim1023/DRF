from django.urls import path
from . import views

urlpatterns = [
	path('', views.ArticleApiView.as_view(), name="blog_api_view"),

]
