from django import forms
from .models import stock

class stockform(forms.ModelForm):
	class Meta:
		model = stock
		fields = ["ticker"]