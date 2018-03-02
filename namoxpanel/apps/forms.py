from __future__ import unicode_literals

from django import forms
from django.conf import settings

from .models import App

class AppForm(forms.ModelForm):

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
