# Generated by Django 2.1.7 on 2019-03-28 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'login',
            },
        ),
    ]
