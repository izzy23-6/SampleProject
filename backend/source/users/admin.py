from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User, Relation
# from Relationships.models import *

# User = get_user_model()

# Register your models here.

admin.site.unregister(Group)

class RelationInline(admin.TabularInline):
    model = Relation
    extra = 1

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    inlines = (RelationInline, )

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    
    list_display = ('username', 'email','full_name', 'created_at', 'last_login', 'jwt_secret', 'created_at', 'facility')
    list_filter = ('staff', 'active',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('staff', 'active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email','full_name','password1', 'password2')}
         ),
    )

    search_fields = ('username', 'full_name')
    # autocomplete_fields = ['custparent']
    ordering = ('username',)
    filter_horizontal = ()

class RelationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'custparent'
    )

admin.site.register(User, UserAdmin)
admin.site.register(Relation, RelationAdmin)

