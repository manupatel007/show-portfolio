from django import forms
from portfolio.models import Project,NewFields

class AddProject(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea())
    technology = forms.CharField(max_length=250)
    source_code = forms.CharField(max_length=50)
    main_image = forms.FileField()
    img1 = forms.FileField()
    img2 = forms.FileField()
    img3 = forms.FileField()

    class Meta:
        model = Project
        fields = ('title','desription','technology','main_image','source_code','img1','img2','img3')
    
class AddFields(forms.Form):
    profile_pic = forms.FileField()
    skills = forms.CharField(max_length=50)
    location = forms.CharField(max_length=100)
    contact = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = NewFields
        fields = ('profile_pic', 'skills', 'location', 'contact', 'bio')

