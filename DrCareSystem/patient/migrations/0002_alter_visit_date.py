# Generated by Django 3.2.2 on 2021-05-08 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
