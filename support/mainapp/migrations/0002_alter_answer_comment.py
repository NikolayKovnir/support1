# Generated by Django 3.2.7 on 2022-02-07 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='comment',
            field=models.TextField(blank=True, default=''),
        ),
    ]
