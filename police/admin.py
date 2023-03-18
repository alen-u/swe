from django.contrib import admin

# Register your models here.
from django.forms import CheckboxSelectMultiple
from django import forms
from .models import *
from django.db import models



#class PoliceForm(forms.ModelForm):
#    password = forms.CharField(widget=forms.PasswordInput)

#    class Meta:
#        model = Police
#        fields = '__all__'



#class PoliceAdmin(admin.ModelAdmin):
#    form = PoliceForm

 #   class Meta:
 #       model = Police


class CaseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
admin.site.register(Police)
admin.site.register(Criminal)