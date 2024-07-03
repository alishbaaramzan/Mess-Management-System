from django.contrib import admin
from .models import Fee,Menu, Meals
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['email', 'name', 'reg_no', 'hostel_no', 'room_no', 'mess_in','staff','admin']
    list_filter = ['admin', 'mess_in']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name','reg_no', 'hostel_no', 'room_no', 'mess_in')}),
        ('Permissions', {'fields': ('admin', 'staff', 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name','reg_no', 'hostel_no', 'room_no', 'mess_in', 'password', 'admin', 'staff', 'is_active')}
        ),
    )
    search_fields = ['email', 'reg_no']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Fee)
admin.site.register(Menu)
admin.site.register(Meals)

