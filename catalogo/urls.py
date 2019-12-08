from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('usuarios/', views.UsuarioListView.as_view(), name='usuarios'),
    path('entrenadores/', views.EntrenadorListView.as_view(), name='entrenadores'),
    path('usuario/<int:pk>', views.UsuarioDetailView.as_view(), name='usuario-detail'),
    path('entrenador/<int:pk>', views.EntrenadorDetailView.as_view(), name='entrenador-detail'),
    
]

urlpatterns += [
    path('usuario/create/', views.UsuarioCreate.as_view(), name='usuario_create'),
    path('usuario/<int:pk>/update/', views.UsuarioUpdate.as_view(), name='usuario_update'),
    path('usuario/<int:pk>/delete/', views.UsuarioDelete.as_view(), name='usuario_delete'),
    path('entrenador/create/', views.EntrenadorCreate.as_view(), name='entrenador_create'),
    path('entrenador/<int:pk>/update/', views.EntrenadorUpdate.as_view(), name='entrenador_update'),
    path('entrenador/<int:pk>/delete', views.EntrenadorDelete.as_view(), name='entrenador_delete'),
]
