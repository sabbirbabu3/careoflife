# Generated by Django 5.0.1 on 2024-03-02 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_appointment_symtom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='symtom',
            field=models.TextField(),
        ),
    ]
