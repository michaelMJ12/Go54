# Generated by Django 4.0.10 on 2023-09-16 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadershipApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(blank=True, max_length=225, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
