from django.urls import path
from . import views

app_name = 'invApp'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create/', views.create_view, name='product_create'),
    path('listings/', views.product_list_view, name='listings'),
    path('update/<int:product_id>/', views.update_view, name='product_update'),
    path('delete/<int:product_id>/', views.delete_view, name='product_delete'),
]
