# Generated by Django 2.1.7 on 2019-04-04 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0005_auto_20190404_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeraddress',
            name='city',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
    ]