# Generated by Django 3.1 on 2020-08-25 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0003_auto_20200822_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takencourse',
            name='grade',
            field=models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Superior', 'Superior'), ('Meritorious', 'Meritorious'), ('Very Good', 'Very Good'), ('Good', 'Good'), ('Very Satisfactory', 'Very Satisfactory'), ('Satisfactory', 'Satisfactory'), ('Fair', 'Fair'), ('Passing', 'Passing'), ('Incomplete', 'Incomplete'), ('Failed', 'Failed'), ('NG', 'NG')], max_length=200),
        ),
    ]
