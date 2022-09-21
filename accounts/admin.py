from django.contrib import admin
from .models import Profile,UserPhoneNumper,UserAdress
# Register your models here.
admin.site.register(Profile)
admin.site.register(UserPhoneNumper)
admin.site.register(UserAdress)