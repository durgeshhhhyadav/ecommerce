# Generated by Django 2.1.7 on 2019-04-02 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0002_producthistory_productordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='productordered',
            name='price',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
    ]
