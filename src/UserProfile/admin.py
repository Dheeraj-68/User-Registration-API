from django.contrib import admin
from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('id','user')

admin.site.register(Profile,ProfileAdmin)
