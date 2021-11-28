from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path ('about/', views.about, name='about'),
    path('dolphins/', views.dolphins_index, name='dolphins_index'),
    path('dolphins/<int:dolphin_id>/', views.dolphins_detail, name='dolphins_detail'),
    path('dolphins/create/', views.DolphinCreate.as_view(), name='dolphins_create'),
    path('dolphins/<int:pk>/update/', views.DolphinUpdate.as_view(), name='dolphins_update'),
    path('dolphins/<int:pk>/delete/', views.DolphinDelete.as_view(), name='dolphins_delete'),
    path('dolphins/<int:dolphin_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    
]