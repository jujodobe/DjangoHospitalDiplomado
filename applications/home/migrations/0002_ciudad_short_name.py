# Generated by Django 4.2.4 on 2023-09-05 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciudad',
            name='short_name',
            field=models.CharField(max_length=5, null=True, verbose_name='Nombre corto'),
        ),
    ]
