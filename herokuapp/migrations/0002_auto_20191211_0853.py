# Generated by Django 2.1.7 on 2019-12-11 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herokuapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='published_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='researches',
            name='published_at',
            field=models.DateField(),
        ),
    ]