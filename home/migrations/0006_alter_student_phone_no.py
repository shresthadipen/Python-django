# Generated by Django 5.1.3 on 2024-11-21 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_student_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_no',
            field=models.BigIntegerField(),
        ),
    ]
