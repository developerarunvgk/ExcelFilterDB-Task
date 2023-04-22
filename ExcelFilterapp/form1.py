from django import forms
from django import forms
import datetime

class CrawlForm(forms.Form):
    code = forms.CharField(label="Enter Code ",max_length=500,required=False)  
    name = forms.CharField(label="Enter Name ",max_length=500,required=False)


class CrawlFormChild(forms.Form):
    name = forms.CharField(label="Enter Name ",max_length=500,required=False)
