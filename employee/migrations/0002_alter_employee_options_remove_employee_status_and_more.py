# Generated by Django 4.0.5 on 2022-06-14 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'EmployeeData'},
        ),
        migrations.RemoveField(
            model_name='employee',
            name='status',
        ),
        migrations.AddField(
            model_name='employee',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
