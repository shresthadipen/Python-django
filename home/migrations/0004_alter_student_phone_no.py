# Generated by Django 5.1.3 on 2024-11-21 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_title_student_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_no',
            field=models.BigIntegerField(),
        ),
    ]
