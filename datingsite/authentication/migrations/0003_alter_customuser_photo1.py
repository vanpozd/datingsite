# Generated by Django 4.1 on 2024-11-23 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_customuser_photo1_customuser_photo2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo1',
            field=models.ImageField(default=None, null=True, upload_to='images/'),
        ),
    ]
