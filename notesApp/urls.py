from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add_person),
    path('show/', views.get_all),
    path('showUsers',views.get_users_api),
    
    path('mainActivities', views.get_Main_Activities),
    path('mainPlot', views.get_Main_Plot),
    path('mainProjectmaster', views.get_Main_ProjectMaster),
    path('mainTreatments', views.get_Main_Treatments),
    path('mainUsers', views.get_Main_Users),
]
