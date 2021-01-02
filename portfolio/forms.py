from django import forms
from portfolio.models import Project

class AddProject(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea())
    technology = forms.CharField(max_length=250)
    image = forms.FileField()
    
    class Meta:
        model = Project
        fields = ('title','desription','technology','image')