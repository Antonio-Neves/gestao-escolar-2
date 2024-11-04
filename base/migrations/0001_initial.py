# Generated by Django 5.0.6 on 2024-07-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaConhecimento',
            fields=[
                ('area_codigo', models.CharField(max_length=2, primary_key=True, serialize=False, unique=True, verbose_name='Código da componente curricular')),
                ('componente_curricular', models.CharField(max_length=50, unique=True, verbose_name='Componente curricular')),
                ('area_conhecimento', models.CharField(max_length=50, verbose_name='Área de conhecimento')),
            ],
            options={
                'verbose_name': 'Componente curricular',
                'verbose_name_plural': 'Componentes curriculares',
                'ordering': ['componente_curricular'],
            },
        ),
        migrations.CreateModel(
            name='AtividadeComplementar',
            fields=[
                ('codigo_area', models.CharField(max_length=2, verbose_name='Código da área')),
                ('nome_area', models.CharField(max_length=50, verbose_name='Nome da área')),
                ('codigo_subarea', models.CharField(max_length=3, verbose_name='Código da sub-área')),
                ('nome_subarea', models.CharField(max_length=50, verbose_name='Nome da área')),
                ('codigo_atividade', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True, verbose_name='Código da atividade')),
                ('nome_atividade', models.CharField(max_length=100, verbose_name='Nome da atividade')),
            ],
            options={
                'verbose_name': 'Atividade complementar',
                'verbose_name_plural': 'Atividades complementares',
                'ordering': ['codigo_area', 'codigo_subarea', 'nome_atividade'],
            },
        ),
        migrations.CreateModel(
            name='CursoFS',
            fields=[
                ('cfs_codigo', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True, verbose_name='Código do Curso de Formação Superior')),
                ('cfs_nome_grau', models.CharField(max_length=100, unique=True, verbose_name='Nome do curso de Formação Superior')),
            ],
            options={
                'verbose_name': 'Curso Formação Superior',
                'verbose_name_plural': 'Cursos de Formação Superior',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('municipio_codigo', models.CharField(max_length=7, primary_key=True, serialize=False, unique=True, verbose_name='Código do Município')),
                ('municipio_uf', models.CharField(max_length=2, verbose_name='UF')),
                ('municipio_nome', models.CharField(max_length=50, verbose_name='Município')),
            ],
            options={
                'verbose_name': 'Município',
                'verbose_name_plural': 'Municípios',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('pais_codigo', models.CharField(max_length=3, primary_key=True, serialize=False, unique=True, verbose_name='Código do País')),
                ('pais_nome', models.CharField(max_length=50, verbose_name='País')),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Países',
            },
        ),
    ]
