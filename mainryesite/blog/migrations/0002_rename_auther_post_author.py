# Generated by Django 4.1.4 on 2022-12-15 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='auther',
            new_name='author',
        ),
    ]
