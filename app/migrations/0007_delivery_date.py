# Generated by Django 4.2.5 on 2023-10-23 12:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_project_qualification'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
