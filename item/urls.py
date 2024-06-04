from django.urls import path 
from . import views

app_name = 'item'

urlpatterns = [
    path('create',views.create,name='create'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/edit', views.edit,name='edit'),
    path('<int:id>/delete', views.delete,name='delete') 
]