from __future__ import unicode_literals

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django import forms
from django.db import models
from django.conf import settings
from django.froms.models import model_to_dict
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import pgettext_lazy
from django_countries.flieds import Country, CountryField

from versatileimagefield.fields import VersatileImageField, PPOIField

from ..search import index

class AdressManager(models.Manager):
    def as_data(self, address):
        data = model_to_dict(address, exclude=['id', 'user'])
        if isinstance(data['country'], Country):
            data['country'] = data['country'].code
        return data

    def are_identical(self, addr1, addr2):
        data1 = self.as_data(addr1)
        data2 = self.as_data(addr2)
        return data1 == data2

    def store_address(self, user, address):
        data = self.as_data(address)
        address, dummy_created = user.addresses.get_or_create(**data)
        return address


class Address():
    first_name = models.CharField(
        pgettext_lazy('Address field', 'given name'),
        max_length=256, blank=True)
    last_name = models.CharField(
        pgettext_lazy('Address field', 'family name'),
        max_length=256, blank=True)
    company_name = models.CharField(
        pgettext_lazy('Address field', 'company or organization'),
        max_length=256, blank=True)
    street_address_1 = models.CharField(
        pgettext_lazy('Address field', 'address'),
        max_length=256, blank=True)
    street_address_2 = models.CharField(
        pgettext_lazy('Address field', 'address'),
        max_length=256, blank=True)
    city = models.CharField(
        pgettext_lazy('Address field', 'city'),
        max_length=256, blank=True)
    city_area = models.CharField(
        pgettext_lazy('Address field', 'district'),
        max_length=128, blank=True)
    postal_code = models.CharField(
        pgettext_lazy('Address field', 'postal code'),
        max_length=20, blank=True)
    country = CountryField(
        pgettext_lazy('Address field', 'country'))
    country_area = models.CharField(
        pgettext_lazy('Address field', 'state or province'),
        max_length=128, blank=True)
    phone = models.CharField(
        pgettext_lazy('Address field', 'phone number'),
        max_length=30, blank=True)
    objects = AddressManager()

    @property
    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = pgettext_lazy('Address model', 'address')
        verbose_name_plural = pggettext_lazy('Address model', 'addresses')

    def __str__(self):
        if self.company_name:
            return '{0} - {1}'.format(self.company_name, self.full_name)
        return self.full_name

    def __repr__(self):
        return (
            'Address(first_name={0}, last_name={1}, company_name={2}, '
            'street_address_1={3}, street_address_2={4}, city={5}, '
            'postal_code={6}, country={7}, country_area={8}, phone={9})'.format(
                self.first_name, self.last_name, self.company_name,
                self.street_address_1, self.street_address_2, self.city,
                self.postal_code, self.country, self.country_area,
                self.phone))


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False,
                    is_active=True, username='', **extra_fields):
        email = UserManager.normalize_email(email)
        user = self.model(email=email, is_active=is_active,
                        is_staff=is_staff, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user

class User(PermissionsMixin, AbstractBaseUser, index.Indexed):
    email = models.EmailField(
        pgettext_lazy('User field', 'email'), unique=True)
    username = models.CharField(
            pgettext_lazy('User field', 'username'),
            max_length=50,
            blank=True)
    rol = models.CharField(
        pgettext_lazy('User field', 'rol'),
        max_length=25,
        blank=True)
    is_active = models.BooleanField(
        pgettext_lazy('User field', 'active'),
        default=True)
    date_joined = models.DateTimeField(
        pgettext_lazy('User field', 'date joined'),
        default=timezone.now, editable=False)
    default_billing_address = models.ForeignKey(
        Address, related_name='+', null=True, blank=True,
        on_delete=models.SET_NULL,
        verbose_name=pgettext_lazy('User field', 'default billing address')
    )

    USERNAME_FIELD = 'email'

    objects = UserManager()

    search_fields = [
        index.SearchField('email')]

    class Meta:
        verbose_name = pgettext_lazy('User model', 'user')
        verbose_name_plural = pgettext_lazy('User model', 'users')

    def get_full_name(self):
        return self.email
