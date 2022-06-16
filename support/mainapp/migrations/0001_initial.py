# Generated by Django 3.2.7 on 2022-02-17 19:53

from django.conf import settings
import django.contrib.auth.password_validation
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=30, validators=[django.contrib.auth.password_validation.validate_password])),
                ('re_password', models.CharField(max_length=30, validators=[django.contrib.auth.password_validation.validate_password])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('body', models.TextField(blank=True, default='')),
                ('answer', models.TextField(blank=True, default='')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
            },
        ),
    ]
