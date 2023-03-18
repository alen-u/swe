from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AnonymousTip, AnonymousUser, Evidence

admin.site.register(AnonymousUser)
admin.site.register(AnonymousTip)
admin.site.register(Evidence)
