# Generated by Django 4.0.2 on 2022-03-02 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='наименование')),
                ('repository_url', models.URLField(verbose_name='ссылка на репозиторий')),
            ],
            options={
                'verbose_name': 'проект',
                'verbose_name_plural': 'проекты',
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='заголовок')),
                ('text', models.TextField(verbose_name='заметка')),
                ('is_active', models.BooleanField(default=True, verbose_name='активна')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project', verbose_name='проект')),
            ],
            options={
                'verbose_name': 'заметка',
                'verbose_name_plural': 'заметки',
            },
        ),
    ]
