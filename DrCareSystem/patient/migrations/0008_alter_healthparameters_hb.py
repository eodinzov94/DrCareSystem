# Generated by Django 3.2.2 on 2021-06-06 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_alter_healthparameters_lymph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthparameters',
            name='HB',
            field=models.FloatField(default=0),
        ),
    ]
