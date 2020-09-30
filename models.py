from django.db import models

from django.urls import reverse

# Create your models here.

class ToDoApp(models.Model):

	title = models.CharField(max_length=45)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse(f"todo:update_todo", kwargs={"id":self.id})