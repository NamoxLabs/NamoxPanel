from __future__ import unicode_literals

from django import forms
from django.utils.translation import pgettext

from .models import App


class AppForm(forms.ModelForm):
    app_name = forms.CharField(max_length=240,
        label=pgettext('App form field', 'App Name'))
    description = forms.CharField(
        label=pgettext('App form field', 'Description'))
    version = forms.CharField(max_length=15,
        label=pgettext('App form field', 'Version'))

    class Meta:
        model = App
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AppForm, self).__init__(*args, **kwargs)
        self.fields['technology'].label = ""
        self.fields['db_engine'].label = ""
        self.fields['db_dump'].label = ""
        self.fields['product'].label = ""
        self.fields['output'].label = ""

    def save(self, commit=True):
        instance = super(AppForm, self).save(commit=commit)
        return instance