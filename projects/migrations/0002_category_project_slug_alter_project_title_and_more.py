# Generated by Django 4.0.6 on 2022-08-01 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='technology',
            name='title',
            field=models.CharField(max_length=25),
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='projects.category'),
        ),
    ]
