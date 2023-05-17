from django import forms
from .models import News


class CreateUpdateForm(forms.ModelForm):

	headlines = forms.CharField(required=True,max_length=50)
	content=forms.CharField(max_length=200)

	class Meta:
		model = News
		fields = ['headlines', 'content']



