# Generated by Django 5.0.1 on 2024-02-08 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureapp', '0003_alter_profile_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='forget_password_token',
            field=models.CharField(default='token123', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pincode',
            field=models.CharField(default='', max_length=150, null=True),
        ),
    ]
