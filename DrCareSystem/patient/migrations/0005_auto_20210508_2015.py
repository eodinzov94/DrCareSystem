# Generated by Django 3.2.2 on 2021-05-08 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_alter_visit_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='visits',
        ),
        migrations.AddField(
            model_name='visit',
            name='patient',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
    ]
