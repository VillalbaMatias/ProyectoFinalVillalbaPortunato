from django.urls import path
from Blog import views


urlpatterns = [
    path('', views.mostrar_herencia, name='Home'),
    path('singup/', views.SingUpView.as_view(), name='SingUp'),
    path('login/', views.AdminLoginView.as_view(), name='Login'),
    path('logout/', views.AdmingLogoutView.as_view(), name='Logout'),
    path('register/', views.SingUpView.as_view(), name='Register'),
    path('addPost/', views.PostCreateView.as_view(), name='AddPost'),
    path('listPost/', views.PostList.as_view(), name='ListPost'),
    path('post_detail/<pk>', views.PostDetailView.as_view(), name='Detail'),
    path('post_update/<pk>', views.PostUpdateView.as_view(), name='Update'),
    path('post_confirm_delete/<pk>', views.PostDeleteView.as_view(), name='Delete'),
    path('editar_usuario/', views.editar_usuario, name='EditUser'),
    
]