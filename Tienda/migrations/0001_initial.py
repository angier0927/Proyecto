# Generated by Django 2.2.3 on 2021-03-23 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=60)),
                ('precio', models.IntegerField(max_length=100)),
                ('categoria', models.CharField(max_length=50)),
                ('disponibilidad', models.CharField(max_length=10)),
                ('descuento', models.IntegerField(max_length=100)),
            ],
        ),
    ]
