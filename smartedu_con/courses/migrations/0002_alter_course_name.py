# Generated by Django 5.1.4 on 2025-02-08 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(help_text='Kurs adını yazınız', max_length=200, unique=True, verbose_name='Kurs Adı '),
        ),
    ]
