from django.urls import path
from . import views

urlpatterns = [
    path('', views.house_list, name='house_list'),
    path('house/<int:house_id>/', views.house_detail, name='house_detail'),
    path('house/<int:house_id>/contact/', views.contact_agent, name='contact_agent'),
]
