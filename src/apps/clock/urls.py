from django.urls import path

from . import views


app_name = 'clock'

urlpatterns = (
    path('<int:pk>/', views.HomeView.as_view(), name='home'),
)