# Generated by Django 4.2.4 on 2023-08-30 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='preview',
            field=models.ImageField(upload_to='media'),
        ),
    ]
