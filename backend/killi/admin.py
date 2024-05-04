from django.contrib import admin

# Register your models here.
from .models import User,Buses,Bus1,Bus2,Bus3
admin.site.register(User)
admin.site.register(Buses)
admin.site.register(Bus1)
admin.site.register(Bus2)
admin.site.register(Bus3)

