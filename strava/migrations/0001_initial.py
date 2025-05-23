# Generated by Django 5.1.6 on 2025-03-18 11:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome.', max_length=100, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Nome')),
                ('email', models.EmailField(help_text='E-mail', max_length=254, unique=True, verbose_name='E-mail')),
                ('generos', models.CharField(choices=[('MAN', 'Homem'), ('WOMAN', 'Mulher'), ('N_BINARY', 'Não Binário'), ('N_INFORM', 'Não informado')], help_text='Genero', max_length=10, verbose_name='Genero')),
                ('cpf', models.CharField(help_text='CPF', max_length=11, validators=[django.core.validators.MinLengthValidator(11)], verbose_name='CPF')),
                ('senha', models.CharField(help_text='Senha', max_length=20, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Senha')),
                ('data_nascimento', models.DateField(help_text='Data de Nascimento.', verbose_name='Data de Nascimento')),
                ('local', models.CharField(default='Porto Alegre', help_text='Cidade', max_length=100, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Cidade')),
                ('pais', models.CharField(default='Brasil', help_text='País', max_length=100, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='País')),
                ('peso', models.FloatField(default=0, help_text='Peso', validators=[django.core.validators.MinValueValidator(20)], verbose_name='Peso')),
                ('pagina_pessoal', models.URLField(default='google.com.br', help_text='Página Pessoal', max_length=150, validators=[django.core.validators.URLValidator(), django.core.validators.MinLengthValidator(15)], verbose_name='Página Pessoal')),
                ('biografia', models.TextField(blank=True, help_text='Biografia - Campo Opicional', verbose_name='Biografia')),
                ('premium', models.BooleanField(default=False, help_text='Premiun', verbose_name='Conta Premiun')),
                ('membro_desde', models.DateField(default=True)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfis',
                'ordering': ('premium', 'nome', 'data_nascimento', 'local', 'pais', 'generos', 'peso', 'membro_desde'),
            },
        ),
    ]
