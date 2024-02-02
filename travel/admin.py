from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Agency)
admin.site.register(Branch)
admin.site.register(Bus_layout)
admin.site.register(Bus)
admin.site.register(Trip)
