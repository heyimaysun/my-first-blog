from django import forms
from . models import ToDo

class ToDoCreate(forms.Form):
    title = forms.CharField()
    body =forms.CharField()
    date = forms.DateTimeField()

class ToDoUpdate(forms.ModelForm):
      class Meta:
          model = ToDo
          fields = ('title','body','date')

