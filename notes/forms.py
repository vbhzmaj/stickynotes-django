from django import forms

from .models import Snote

class NotesForm(forms.ModelForm):
    class Meta:
        model = Snote
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control my-5'}),
            'content': forms.Textarea(attrs={'class':'form-control mb-5'})
        }
        labels = {
            'content':"Your idea is:"
        }


    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise forms.ValidationError('We only accept notes about Django!')
        return title