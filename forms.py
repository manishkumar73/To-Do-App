from django import forms

from .models import ToDoApp


class ToDoAppForm(forms.ModelForm):


	title = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Your Task'}))

	class Meta:
		model = ToDoApp
		fields = '__all__'
