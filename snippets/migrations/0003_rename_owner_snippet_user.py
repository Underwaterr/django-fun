# Generated by Django 3.2 on 2021-04-21 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_snippet_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='owner',
            new_name='user',
        ),
    ]