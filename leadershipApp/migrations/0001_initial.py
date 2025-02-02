# Generated by Django 4.0.10 on 2023-09-15 20:15

from django.db import migrations, models
import leadershipApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ceo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=225)),
                ('course_price', models.CharField(blank=True, max_length=225)),
                ('course_description', models.TextField(blank=True, max_length=1000)),
                ('duration', models.CharField(blank=True, max_length=225)),
                ('start_date', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=225)),
                ('email', models.EmailField(blank=True, max_length=225, unique=True)),
                ('subject', models.CharField(blank=True, max_length=225)),
                ('message', models.TimeField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='StudentRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, max_length=225, null=True)),
                ('month', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('course', models.CharField(blank=True, max_length=225, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=225, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('current_program', models.CharField(blank=True, max_length=500, null=True)),
                ('academic_performance', models.CharField(blank=True, max_length=500, null=True)),
                ('area_of_specializations', models.CharField(blank=True, max_length=500, null=True)),
                ('leadership_positions_held', models.CharField(blank=True, max_length=200, null=True)),
                ('duration_of_leadership_roles', models.CharField(blank=True, max_length=255, null=True)),
                ('leadership_achievements_and_responsibilities', models.CharField(blank=True, max_length=255, null=True)),
                ('year_of_study', models.IntegerField(null=True)),
                ('age', models.IntegerField(null=True)),
                ('state', models.CharField(blank=True, max_length=225, null=True)),
                ('country', models.CharField(blank=True, max_length=225, null=True)),
                ('resume_cv_upload', models.FileField(null=True, upload_to='resumes')),
                ('file_uploads', models.FileField(null=True, upload_to='additional_files')),
                ('image', models.ImageField(null=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='media')),
                ('phone', models.CharField(blank=True, max_length=225)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('is_staff', models.BooleanField(blank=True, default=False)),
                ('date_joined', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', leadershipApp.models.CustomUserManager()),
            ],
        ),
    ]
