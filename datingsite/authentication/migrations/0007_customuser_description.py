# Generated by Django 4.1 on 2024-12-15 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_customuser_hobby_customuser_inst_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='description',
            field=models.TextField(default=None, null=True),
        ),
    ]
