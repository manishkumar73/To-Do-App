from django.urls import path

from .views import (

	index,
	UpdateToDo,
	deleteTask,

	)


app_name = 'todo'
urlpatterns = [

	path('', index , name='indexoftodo'),
	path('todo/<str:pk>/', UpdateToDo, name='update_todo'),
	path('delete/<str:pk>/', deleteTask, name="delete"),

]