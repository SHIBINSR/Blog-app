# Generated by Django 5.1.4 on 2024-12-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogHome', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
