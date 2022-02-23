from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Profile, Wish, Commitment


class ProfileInline(admin.StackedInline):
	model = Profile


class UserAdmin(admin.ModelAdmin):
	model = User 
	fields = ["username"]
	inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Wish)
admin.site.register(Commitment)
