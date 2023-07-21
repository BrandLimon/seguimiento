# Generated by Django 4.2.3 on 2023-07-21 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apepat', models.CharField(max_length=15)),
                ('apemat', models.CharField(max_length=15)),
                ('matric', models.CharField(max_length=10)),
                ('numcedula', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apepat', models.CharField(max_length=15)),
                ('apemat', models.CharField(max_length=15)),
                ('matric', models.CharField(max_length=6)),
                ('direccion', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=10)),
            ],
        ),
    ]