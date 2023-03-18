from django import forms
from .models import Case

class case_form(forms.ModelForm):
    class Meta:
        model=Case
        fields="__all__"
        exclude = ['approved','userid','updated','timestamp','solved']

    def __init__(self, *args, **kwargs):
        super(case_form, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            "name":"title"})
        self.fields['case_categories'].widget.attrs.update({
            'class': 'form-control',
            "name":"case_categories"})
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            "name":"description"})
        self.fields['reg_from_loc'].widget.attrs.update({
            'class': 'form-control',
            "name":"reg_from_loc"})

