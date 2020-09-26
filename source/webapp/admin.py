from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from accounts.models import Profile
from webapp.models import Product, Review


class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ['avatar', 'about', 'github_profile']


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]


admin.site.register(Product)
admin.site.register(Review)
admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
