# Generated by Django 5.1.2 on 2024-11-09 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test11app', '0003_checktab_original_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='checktab',
            name='is_modified',
            field=models.BooleanField(default=False),
        ),
    ]