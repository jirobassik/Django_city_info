from django.urls import path
from . import views

urlpatterns = [
    path('', views.object_view, name="tables"),
    path('search/', views.search, name='search_table'),
    path('create/', views.ObjectCreate.as_view(), name='create_table'),
    path('delete/<int:id>', views.delete_object, name='object-delete'),
    path('edit/<int:pk>', views.ObjectUpdate.as_view(), name='object-update'),
]
