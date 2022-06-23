from django.urls import path
from product import views
urlpatterns = [
    path('', views.ProductView.as_view(), name='event_api_view'),
    path('<obj_id>/', views.ProductView.as_view()),
    path('thumbnail/<obj_id>/', views.ProductThumbnailView.as_view(), name='thumbnail_view'),
    # path('', views.EventApiView.as_view(), name='event_api_view'),
    # path('<obj_id>/', views.EventApiView.as_view()),
