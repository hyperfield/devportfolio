# Generated by Django 4.0.6 on 2022-08-02 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_simple_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='simple_url',
            new_name='url_name',
        ),
    ]
