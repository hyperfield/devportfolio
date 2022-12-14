# Generated by Django 4.0.6 on 2022-08-22 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_technology_logotype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['priority'], 'verbose_name_plural': 'projects'},
        ),
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Priority'),
        ),
    ]
