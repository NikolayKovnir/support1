# Generated by Django 3.2.7 on 2021-11-13 00:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='content',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='status',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='title',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='user',
        ),
        migrations.AddField(
            model_name='ticket',
            name='message',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='ticket',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]