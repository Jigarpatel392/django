# Generated by Django 2.1.5 on 2019-11-11 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FBV', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='dob',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
