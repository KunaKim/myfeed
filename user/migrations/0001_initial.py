# Generated by Django 3.1.5 on 2021-01-12 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='사용자명')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('registeredTime', models.DateTimeField(auto_now_add=True, verbose_name='등록 시간')),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
