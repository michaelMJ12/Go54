# Generated by Django 4.0.10 on 2024-06-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadershipApp', '0004_rename_student_full_name_studentrecord_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrecord',
            name='file_uploads',
            field=models.FileField(null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='studentrecord',
            name='resume_cv_upload',
            field=models.FileField(null=True, upload_to='media'),
        ),
    ]
