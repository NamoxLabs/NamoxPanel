from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import pgettext
from django.contrib.auth import forms as django_forms

from namoxpanel.userprofile.models import User, Address

class LoginForm(django_forms.AuthenticationForm):
    username = forms.EmailField(
        label=pgettext('Form field', 'Email'), max_length=75)

    def __init__(self, request=None, *args, **kwargs):
        super(LoginForm, self).__init__(request=request, *args, **kwargs)
        if request:
            email = request.GET.get('email')
            if email:
                self.fields['username'].initial = email

class DirectionForm(forms.ModelForm):
    first_name = forms.CharField(
        label=pgettext('Direction form field', 'Nombre'),
        widget=forms.TextInput)
    last_name = forms.CharField(
        label=pgettext('Direction form field', 'Apellido'),
        widget=forms.TextInput)
    company_name = forms.CharField(
        label=pgettext('Direction form field', 'Empresa'),
        widget=forms.TextInput)
    street_address_1 = forms.CharField(
        required=False,
        label=pgettext('Direction form field', 'Direccion'),
        widget=forms.TextInput)
    street_address_2 = forms.CharField(
        label=pgettext('Direction form field', 'Direccion2'),
        widget=forms.Select)
    city = forms.CharField(
        label=pgettext('Direction form field', 'Ciudad'),
        widget=forms.TextInput)
    city_area = forms.CharField(
        label=pgettext('Direction form field', 'Ciudad Area'),
        widget=forms.TextInput)
    postal_code = forms.CharField(
        label=pgettext('Direction form field', 'Código Postal'),
        widget=forms.TextInput)
    country = forms.CharField(
        label=pgettext('Direction form field', 'País'),
        widget=forms.TextInput)
    country_area = forms.CharField(
        label=pgettext('Direction form field', 'Área País'),
        widget=forms.TextInput)
    phone = forms.CharField(
        label=pgettext('Direction form field', 'Teléfono'),
        widget=forms.TextInput)

    class Meta:
        model = Address
        fields = ('first_name', 'last_name', 'company_name',
            'street_address_1', 'street_address_2', 'city', 'city_area', 'postal_code', 'country', 'country_area', 'phone')

    def __init__(self, *args, **kwargs):
        super(DirectionForm, self).__init__(*args, **kwargs)

class SignupForm(forms.ModelForm):
    password = forms.CharField(
        label=pgettext('User form field', 'Contraseña'),
        widget=forms.PasswordInput)
    repassword = forms.CharField(
        label=pgettext('User form field', 'Confirmar Contraseña'),
        widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email', 'password',)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update(
                {'autofocus': ''})

    def save(self, request=None, commit=True):
        user = super(SignupForm, self).save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        user.email = self.cleaned_data['email']
        user.is_staff = False

        if commit:
            user.save()
        return user

class SetPasswordForm(django_forms.SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)
        del self.fields['new_password2']
