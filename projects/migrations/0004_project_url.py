# Generated by Django 4.0.6 on 2022-08-01 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_category_options_alter_project_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
