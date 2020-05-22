# Generated by Django 3.0.5 on 2020-05-18 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11)),
                ('nascimento', models.DateField()),
                ('login_crm', models.CharField(max_length=255)),
                ('senha_crm', models.CharField(max_length=255)),
                ('id_fast', models.IntegerField()),
                ('permissao', models.CharField(max_length=255)),
                ('skill', models.CharField(max_length=255)),
                ('empresa', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('telefone1', models.CharField(max_length=12)),
                ('telefone2', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'cadastro_usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ponto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=255)),
                ('horario', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'ponto_eletronico',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissao', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cadastro_usuario',
                'managed': False,
            },
        ),
    ]
