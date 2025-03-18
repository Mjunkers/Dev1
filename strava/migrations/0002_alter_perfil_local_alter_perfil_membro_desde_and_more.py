# Generated by Django 5.1.6 on 2025-03-18 11:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strava', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='local',
            field=models.CharField(help_text='Cidade', max_length=100, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='membro_desde',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='pagina_pessoal',
            field=models.URLField(help_text='Página Pessoal', max_length=150, validators=[django.core.validators.URLValidator(), django.core.validators.MinLengthValidator(15)], verbose_name='Página Pessoal'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='pais',
            field=models.CharField(help_text='País', max_length=100, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='País'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='peso',
            field=models.FloatField(help_text='Peso', validators=[django.core.validators.MinValueValidator(20)], verbose_name='Peso'),
        ),
    ]
