# import form class from django
from django import forms
from ckeditor.fields import RichTextField
# import GeeksModel from models.py
from .models import discussion_room, conversation

# create a ModelForm
class Roomforms(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = discussion_room
		fields = ('name', 'description', 'cover_img',)
		widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':' Your Email', 'required':'required'}),
        }

class Coversationform(forms.ModelForm) :
	class Meta:
		model = conversation
		fields = ('text',)
		