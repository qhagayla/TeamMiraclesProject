# Generated by Django 4.0.8 on 2023-11-07 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_courseoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('Regular', 'Regular Student'), ('Student', 'Irregular Student')], max_length=25, null=True),
        ),
    ]