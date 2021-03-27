from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    # logout
    path('logout/', views.logoutuser, name='logoutuser'),
    # login
    path('login/', views.loginuser, name='loginuser'),

    # Todos
    path('current/', views.currenttodos, name='currenttodos'),
    path('completed/', views.completedtodos, name='completedtodos'),
    path('create/', views.createtodo, name='createtodo'),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),

    # homepage
    path('', views.home, name='home'),
]