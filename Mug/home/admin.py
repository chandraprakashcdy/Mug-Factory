from django.contrib import admin
from .models import Mug, UserProfile, Factory

# Register your models here.
admin.site.register(Mug)
admin.site.register(Factory)
admin.site.register(UserProfile)
