# Generated by Django 4.0.6 on 2022-08-13 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_alter_image_options_alter_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='projects.project'),
        ),
    ]
