# Generated by Django 5.1.6 on 2025-03-17 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='Descrição para umm exemplo.', max_length=100, verbose_name='Descrição')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
