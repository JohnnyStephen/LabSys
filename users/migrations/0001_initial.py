# Generated by Django 2.1.2 on 2018-10-26 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models.user


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('roles', '0001_initial'),
        ('teaching_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(db_column='class_id', on_delete=django.db.models.deletion.CASCADE, to='teaching_info.ClassInfo')),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=11, unique=True, validators=[users.models.user.validate_mobile_num])),
                ('photo', models.FilePathField(unique=True)),
                ('birth_day', models.DateField()),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.roles.Role')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
    ]
