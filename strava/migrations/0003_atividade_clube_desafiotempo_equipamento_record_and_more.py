# Generated by Django 5.1.6 on 2025-05-19 22:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strava', '0002_alter_perfil_local_alter_perfil_membro_desde_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome', max_length=100, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Nome')),
                ('observacoes', models.CharField(help_text='Observações', max_length=100, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Opicional')),
                ('data', models.DateField(help_text='Data do Exercício', verbose_name='Data')),
                ('esporte', models.CharField(choices=[('Corrida', 'Corrida'), ('TRAIL', 'Trilha'), ('BIKE', 'Treino de Bicicleta'), ('WALK', 'Caminhada'), ('HIT', 'Treinamento de Alta Intensidade'), ('STRENGTH', 'Treino de Força'), ('CARDIO', 'Treino Aeróbico'), ('SWIMMING', 'Natação')], help_text='Tipos de Esporte', max_length=50, verbose_name='Esporte')),
                ('duracao', models.TimeField(help_text='Tempo em exercício', verbose_name='Duração')),
                ('distancia', models.FloatField(default=0, help_text='Distancia total', verbose_name='Distancia percorrida')),
                ('ritmo', models.TimeField(help_text='Pace', verbose_name='Ritmo')),
                ('calorias', models.IntegerField(default=0, help_text='Calorias gastas no execício', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Calorias')),
                ('elevacao', models.IntegerField(default=0, help_text='--', verbose_name='Elevação')),
            ],
            options={
                'verbose_name': 'Atividade',
                'verbose_name_plural': 'Atividades',
            },
        ),
        migrations.CreateModel(
            name='Clube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do Clube', max_length=100, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Clube')),
                ('local', models.CharField(help_text='Cidade', max_length=100, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Cidade')),
                ('pais', models.CharField(help_text='País', max_length=100, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='País')),
                ('biografia', models.TextField(blank=True, help_text='Biografia - Campo Opicional', verbose_name='Biografia')),
                ('site', models.URLField(help_text='Página Web do Clube', max_length=150, validators=[django.core.validators.MinLengthValidator(15)], verbose_name='Página do Clube')),
                ('esporte', models.CharField(choices=[('Corrida', 'Corrida'), ('TRAIL', 'Trilha'), ('BIKE', 'Treino de Bicicleta'), ('WALK', 'Caminhada'), ('HIT', 'Treinamento de Alta Intensidade'), ('STRENGTH', 'Treino de Força'), ('CARDIO', 'Treino Aeróbico'), ('SWIMMING', 'Natação')], help_text='Tipos de Esporte', max_length=50, verbose_name='Esporte')),
            ],
            options={
                'verbose_name': 'Clube',
                'verbose_name_plural': 'Clube',
            },
        ),
        migrations.CreateModel(
            name='DesafioTempo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome', max_length=50, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Nome')),
                ('data_inicio', models.DateField(help_text='Data de Início', verbose_name='Data de Início')),
                ('esporte', models.CharField(choices=[('Corrida', 'Corrida'), ('TRAIL', 'Trilha'), ('BIKE', 'Treino de Bicicleta'), ('WALK', 'Caminhada'), ('HIT', 'Treinamento de Alta Intensidade'), ('STRENGTH', 'Treino de Força'), ('CARDIO', 'Treino Aeróbico'), ('SWIMMING', 'Natação')], help_text='Tipo de Esporte', max_length=20, verbose_name='Esporte')),
                ('visao_geral', models.TextField(help_text='Resumo', verbose_name='Resumo do Desafio')),
                ('selo', models.CharField(help_text='Selo', max_length=5, verbose_name='Selo')),
                ('meta_duracao', models.TimeField(help_text='Tempo em exercício', verbose_name='Duração')),
            ],
            options={
                'verbose_name': 'Desafio de Tempo',
                'verbose_name_plural': 'Desafios de Tempo',
            },
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome', max_length=50, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Nome')),
                ('marca', models.CharField(help_text='Marca', max_length=50, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Marca')),
                ('modelo', models.CharField(help_text='Modelo', max_length=50, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Modelo')),
                ('apelido', models.CharField(help_text='Apelido', max_length=50, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Apelido')),
                ('equipamento', models.CharField(choices=[('TENIS', 'Tênis'), ('BIKE', 'Bicicleta'), ('DEVICE', 'Dipositivo inteligente: Celular, relogio, pulseira ..')], help_text='Tipos de Equipamento', max_length=50, verbose_name='Equipamento')),
                ('esporte', models.CharField(choices=[('Corrida', 'Corrida'), ('TRAIL', 'Trilha'), ('BIKE', 'Treino de Bicicleta'), ('WALK', 'Caminhada'), ('HIT', 'Treinamento de Alta Intensidade'), ('STRENGTH', 'Treino de Força'), ('CARDIO', 'Treino Aeróbico'), ('SWIMMING', 'Natação')], help_text='Tipos de Esporte', max_length=50, verbose_name='Esporte')),
                ('distancia_total', models.FloatField(default=0, help_text='Distancia total', verbose_name='Distancia percorrida')),
                ('distancia_prevista', models.IntegerField(default=400, help_text='Minimo Desejavél', verbose_name='Distancia Mínima')),
                ('peso', models.FloatField(help_text='Peso', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Peso')),
                ('notas', models.TextField(blank=True, help_text='Notas', verbose_name='Notas')),
            ],
            options={
                'verbose_name': 'Equipamento',
                'verbose_name_plural': 'Equipamentos',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome', max_length=20, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Nome')),
                ('marca', models.CharField(choices=[('100M', '100 Metros'), ('400M', '400 Metros'), ('1KM', '1 Quilômetro'), ('5KM', '5 Quilômetros'), ('10KM', '10 Quilômetros'), ('15KM', '15 Quilômetros'), ('20KM', '20 Quilômetros'), ('MEIA MARATONA', 'Meia Maratona'), ('30KM', '30 Quilômetros'), ('MARATONA', 'Maratona'), ('LONGA DISTANCIA', 'Maior distância'), ('LONGA DURACAO', 'Maior duração')], help_text='Tipo de Record', max_length=15, verbose_name='Record')),
                ('esporte', models.CharField(choices=[('Corrida', 'Corrida'), ('TRAIL', 'Trilha'), ('BIKE', 'Treino de Bicicleta'), ('WALK', 'Caminhada'), ('HIT', 'Treinamento de Alta Intensidade'), ('STRENGTH', 'Treino de Força'), ('CARDIO', 'Treino Aeróbico'), ('SWIMMING', 'Natação')], help_text='Tipos de Esporte', max_length=50, verbose_name='Esporte')),
                ('duracao', models.TimeField(help_text='Tempo em exercício', verbose_name='Duração')),
                ('ritmo', models.TimeField(help_text='Pace', verbose_name='Ritmo')),
            ],
            options={
                'verbose_name': 'Record',
                'verbose_name_plural': 'Recordes',
            },
        ),
        migrations.AlterModelOptions(
            name='perfil',
            options={'verbose_name': 'Perfil', 'verbose_name_plural': 'Perfis'},
        ),
    ]
