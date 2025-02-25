# Generated by Django 4.1 on 2024-12-22 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='hobby',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='inst',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='liked_profiles',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='main_goal',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='reported',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='telegram',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='x_network',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
