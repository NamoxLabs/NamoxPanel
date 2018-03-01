from django.utils.translation import pgettext_lazy
from django.utils import timezone
from django.db import models

# Create your models here.
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
    TECH_CHOICES = (
        ('python', 'Python'),
        ('-', '------'),
        ('flask', 'Flask'),
        ('django', 'Django'),
        ('drf', 'Django Rest Framework'),
        ('django_drf', 'Django With Django Rest Framework'),
        ('apistar', 'Apistar'),
        ('php', 'PHP'),
        ('-', '------'),
        ('plain_php', 'Plan PHP'),
        ('plain_php_7', 'Plan PHP 7'),
        ('slim_php', 'Slim PHP'),
        ('ci_php', 'CodeIgniter'),
        ('symfony', 'Symfony'),
        ('yii', 'Yii'),
        ('yii_2', 'Yii 2'),
        ('wp', 'WordPress'),
        ('go', 'Go'),
        ('-', '------'),
        ('js', 'JavaScript'),
        ('-', '------')
    )
    technology = models.CharField(
        choices=TECH_CHOICES,
        max_length=200,
        blank=True,
        null=True,
        default='flask')
    stack = models.BooleanField(
        default=False)
    DATABASE_CHOICES = (
        ('postgres', 'PostgreSQL'),
        ('mysql', 'MySql'),
        ('mariadb', 'MariaDB'),
        ('sqlite', 'SQLite')
    )
    db_engine = models.CharField(
        choices=DATABASE_CHOICES,
        max_length=200,
        blank=True,
        null=True,
        default='postgres')
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
    TECHNOLOGY_CHOICES = (
        ('rest', 'REST'),
        ('soap', 'SOAP'),
        ('websocket', 'WebSocket'),
        ('e-commerce', 'E-Commerce'),
        ('e-commerce-api', 'E-commerce API'),
        ('blog', 'Blog'),
        ('blog-api', 'Blog API'),
        ('personal-page', 'Personal Page')
    )
    technology = models.CharField(
        choices=TECHNOLOGY_CHOICES,
        max_length=200,
        blank=True,
        null=True,
        default='rest'
    )
    OUTPUT_CHOICES = (
        ('json', 'JSON'),
        ('yalm', 'YALM'),
    )
    output = models.CharField(
        choices=OUTPUT_CHOICES,
        max_length=200,
        blank=True,
        null=True,
        default='json'
    )
    request_log = models.BooleanField(
                default=True)
    is_active = models.BooleanField(
                default=True)
    date_created = models.DateTimeField(
                default=timezone.now,
                editable=False)

    class Meta:
        verbose_name = pgettext_lazy('App model', 'app')
        verbose_name_plural = pgettext_lazy('Apps model', 'apps')
