from django.contrib import admin
from authorization.models import DrAccount
# class UsersAdmin(admin.ModelAdmin):
#     list_display = (
#         'username',
#         'data_joined',
#         'is_active',
#         'first_name',
#         'last_name',
#         'dr_license',
#         )
#     fields = ('username','first_name','last_name','dr_license','is_admin',"is_staff","is_superuser","password")
#     list_filter = ('data_joined','is_active',)
#     search_fields = ['username','first_name','last_name','dr_license']
#     ordering = ('username','data_joined')
#     filter_horizontal = ()
# admin.site.register(DrAccount,UsersAdmin)

from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField



class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = DrAccount
        fields = ('username', 'first_name','last_name','person_ID','is_doctor','is_admin')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username','first_name','last_name','person_ID','is_doctor','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username',)}),
        ('Personal info', {'fields': ('first_name','last_name','person_ID',)}),
        ('Permissions', {'fields': ('is_admin','is_doctor')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','first_name','last_name','person_ID', 'password1', 'password2')}
        ),
    )
    search_fields = ('username','first_name','last_name','person_ID')
    ordering = ('username','data_joined')
    filter_horizontal = ()

admin.site.register(DrAccount, UserAdmin)
admin.site.unregister(Group)