# Generated by Django 5.1.4 on 2024-12-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogHome', '0005_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(),
        ),
    ]
