# Generated by Django 4.0.5 on 2022-06-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_alter_employee_joining_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(default='a.png', upload_to='image/'),
        ),
    ]
