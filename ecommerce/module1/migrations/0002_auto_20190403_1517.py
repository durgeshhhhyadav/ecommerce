# Generated by Django 2.1.7 on 2019-04-03 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtocart',
            name='quantity',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addtocart',
            name='quantityprice',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producthistory',
            name='quantity',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producthistory',
            name='quantityprice',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productordered',
            name='quantity',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productordered',
            name='quantityprice',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
    ]