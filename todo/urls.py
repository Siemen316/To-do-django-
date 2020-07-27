from . import views
from django.urls import path


urlpatterns = [
    path('',views.index,name='home'),
    path('addTodo',views.addTodo,name='adddTodo'),
    path('deleteTodo/<int:todo_id>/',views.deleteTodo,name='deleteTodo'),
    path('contact',views.contact,name='contact'),


]
