from django.utils.translation import pgettext_lazy
from django.db import models

from namoxpanel.userprofile.models import User

TECH_CHOICES = (
    ('-', 'Technology'),
    ('flask', 'Flask - Python'),
    ('django', 'Django - Python'),
    ('drf', 'Django Rest Framework - Python'),
    ('django_drf', 'Django With Django Rest Framework - Python'),
    ('apistar', 'Apistar - Python'),
    ('plain_php', 'Plain PHP - PHP'),
    ('plain_php_7', 'Plain PHP 7 - PHP'),
    ('mamp_php', 'MAMP - PHP'),
    ('lamp_php', 'LAMP - PHP'),
    ('slim_php', 'Slim PHP - PHP'),
    ('ci_php', 'CodeIgniter - PHP'),
    ('symfony', 'Symfony - PHP'),
    ('yii', 'Yii - PHP'),
    ('yii_2', 'Yii 2 - PHP'),
    ('wp', 'WordPress - PHP'),
    ('buffalo-go', 'Buffalo - Go'),
    ('mean-js', 'MEAN - JavaScript'),
    ('apollo-server-js', 'Apollo Server - JavaScript'),
    ('parse-js', 'Parse - JavaScript')
)
OUTPUT_CHOICES = (
    ('-', 'Output Data Format'),
    ('json', 'JSON'),
    ('xml', 'XML'),
    ('yalm', 'YALM'),
)
DATABASE_CHOICES = (
    ('-', 'Database'),
    ('postgres', 'PostgreSQL'),
    ('mysql', 'MySql'),
    ('mariadb', 'MariaDB'),
    ('sqlite', 'SQLite')
)
PRODUCT_CHOICES = (
    ('-', 'Product'),
    ('rest', 'REST'),
    ('soap', 'SOAP'),
    ('websocket', 'WebSocket'),
    ('e-commerce', 'E-Commerce'),
    ('e-commerce-api', 'E-commerce API'),
    ('blog', 'Blog'),
    ('blog-api', 'Blog API'),
    ('personal-page', 'Personal Page')
)


# Main object creation
class App(models.Model):
    app_name = models.CharField(
        max_length=240,
        unique=True)
    description = models.TextField(
        blank=True,
        null=True)
    version = models.CharField(
        max_length=15,
        unique=True,
        blank=True,
        null=True,
        default='1.0')
    technology = models.CharField(
        choices=TECH_CHOICES,
        max_length=200,
        blank=True,
        null=True,
        default='-')
    stack = models.BooleanField(
        default=False)
    db_engine = models.CharField(
        choices=DATABASE_CHOICES,
        max_length=200,
        blank=True,
        null=True,
        default='-')
    db_name = models.CharField(
        max_length=180,
        blank=True,
        null=True)
    db_dump = models.FileField(
        upload_to='uploads/',
        null=True,
        blank=True)
    git_repo = models.TextField(
        blank=True,
        null=True)
    dockerized = models.BooleanField(
        default=False)
    admin_panel = models.BooleanField(
        blank=True,
        default=False)
    product = models.CharField(
        choices=PRODUCT_CHOICES,
        max_length=200,
        blank=True,
        default='-')
    output = models.CharField(
        choices=OUTPUT_CHOICES,
        max_length=200,
        blank=True,
        null=True,
        default='-')
    request_log = models.BooleanField(
        default=True)
    active = models.BooleanField(
        blank=False,
        null=False,
        default=True)
    created_by = models.ForeignKey(
        User,
        related_name='app_creator', 
        null=True, blank=True,
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now=True)
    last_update = models.DateTimeField(
        auto_now=True)

    class Meta:
        verbose_name = pgettext_lazy('App model', 'app')
        verbose_name_plural = pgettext_lazy('Apps model', 'apps')
