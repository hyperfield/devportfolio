# Generated by Django 4.0.6 on 2022-10-14 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatido', '0002_alter_taskcategory_options_taskcategory_priority_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['priority']},
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0, verbose_name='Priority'),
        ),
    ]
