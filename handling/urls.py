from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("todos/<int:session>/<str:year>/<str:month>", views.todos, name="todos"),
    path("todo", views.add_delete_todo, name="add_delete_todo"),

    path('is-auth', views.is_logged_in, name="is_logged_in"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("registration", views.register, name="register"),
]
