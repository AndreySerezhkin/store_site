from django.urls import path
from .endpoint import views, auth_views

urlpatterns = [
    path('', views.google_login),
    path('me/', views.UserView.as_view({'get': 'retrieve', 'put': 'update'}))
]