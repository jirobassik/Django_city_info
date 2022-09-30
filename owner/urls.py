from django.urls import path
from . import views

urlpatterns = [
    path('', views.owner_view, name="tables_owner"),
    path('create/', views.OwnerCreate.as_view(), name='create_owner'),
    path('delete/<int:id>', views.delete_owner, name='owner-delete'),
    path('edit/<int:pk>', views.OwnerUpdate.as_view(), name='owner-update'),
]