# Generated by Django 2.1.7 on 2019-03-29 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0004_auto_20190329_1257'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Signup',
            new_name='LoginData',
        ),
        migrations.AlterModelTable(
            name='logindata',
            table=None,
        ),
    ]
