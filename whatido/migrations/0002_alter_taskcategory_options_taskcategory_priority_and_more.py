# Generated by Django 4.0.6 on 2022-10-14 19:51

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('whatido', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskcategory',
            options={'ordering': ['priority'], 'verbose_name_plural': 'Task Categories'},
        ),
        migrations.AddField(
            model_name='taskcategory',
            name='priority',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0, verbose_name='Priority'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='whatido.taskcategory'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_desc',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='taskcategory',
            name='category_desc',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]