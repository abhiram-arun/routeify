from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    
    path('user/', views.getUser),
    path('buses/', views.getBuses),
    path('bus1/', views.getBus1),
    path('bus2/', views.getBus2),
    path('bus3/', views.getBus3),
    
    path('user/create/', views.createUser),
    path('buses/create/', views.createBuses),
    path('bus1/create', views.createBus1),
    path('bus2/create/', views.createBus2),
    path('bus3/create/', views.createBus3),
    
    path('backend/<str:pk>/update',views.updateUser),
    
    path('user/<str:pk>/', views.sgetUser),
    path('buses/<str:pk>/', views.sgetBuses),
    path('bus1/<str:pk>/', views.sgetBus1),
    path('bus2/<str:pk>/', views.sgetBus2),
    path('bus3/<str:pk>/', views.sgetBus3),
    
]