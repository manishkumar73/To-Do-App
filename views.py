from django.shortcuts import render, redirect

# Create your views here.

from .models import *
from .forms import *




def index(request):
	task = ToDoApp.objects.all()
	form = ToDoAppForm()

	if request.method == 'POST':
		form = ToDoAppForm(request.POST or None)
		if form.is_valid():
			form.save()
			form = ToDoAppForm()

	context = {
		'tasks': task,
		'form' : form
	}
	return render(request, 'todo/list.html' , context)



def UpdateToDo(request, pk):

	task = ToDoApp.objects.get(id=pk)

	form = ToDoAppForm(instance=task)

	if request.method == 'POST':
		form = ToDoApp(request.POST , instance=task)
		if form.is_valid():
			form.save()
		    

	context = {	'form':form}
	return render(request, 'todo/updatetodo.html' , context)



def deleteTask(request, pk):
	item = ToDoApp.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'todo/delete.html', context)

