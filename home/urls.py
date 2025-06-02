from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.PlanList, name="plans"),
    path('',views.homeView,name='home-view')
]