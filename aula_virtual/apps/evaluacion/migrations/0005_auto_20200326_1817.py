# Generated by Django 2.2.5 on 2020-03-26 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0004_remove_pregunta_anexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opciones',
            name='descripcion',
            field=models.CharField(max_length=50),
        ),
    ]