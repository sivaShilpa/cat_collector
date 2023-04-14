from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name = 'about'),
  path('cats/', views.cats_index, name = 'index'),
  path('cats/<int:cat_id>/', views.cats_detail, name = 'detail'),
  path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
  path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
  path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
  path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy')
]