# Generated by Django 3.2.4 on 2021-06-26 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kadai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruits',
            name='memo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='メモ'),
        ),
    ]
