# Generated by Django 3.2.2 on 2021-05-18 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_alter_patient_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthparameters',
            name='LYMPH',
            field=models.IntegerField(default=0),
        ),
    ]
