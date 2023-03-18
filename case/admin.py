from django.contrib import admin

# Register your models here.
from django.forms import CheckboxSelectMultiple
from django.db import models

from .models import Case, CaseCategory,Evidence,Witness


class CaseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
admin.site.register(Case,CaseAdmin)
admin.site.register(CaseCategory)
admin.site.register(Evidence)
admin.site.register(Witness)

