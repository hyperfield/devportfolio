# Generated by Django 4.0.6 on 2022-08-02 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='simple_url',
            field=models.CharField(blank=True, max_length=247, null=True),
        ),
    ]
