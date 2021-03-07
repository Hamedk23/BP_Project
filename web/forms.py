from django import forms 
from .models import *

class getanswer(forms.ModelForm):
    class Meta:
        model=Answer
        fields=[
            "name",
            "caption",
            "pdffile"
        ]
class getanswer2(forms.Form):
    name    =forms.CharField(widget=forms.TextInput(attrs={"placeholder": "name of file"}))
    caption =forms.CharField(required=False,widget=forms.Textarea(attrs={"placeholder": "Description"}))
    pdffile =forms.FileField()
