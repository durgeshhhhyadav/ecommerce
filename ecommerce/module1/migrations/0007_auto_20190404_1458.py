# Generated by Django 2.1.7 on 2019-04-04 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0006_customeraddress_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customeraddress',
            old_name='linkAttr',
            new_name='linkUserid',
        ),
        migrations.RemoveField(
            model_name='customeraddress',
            name='userid',
        ),
    ]
