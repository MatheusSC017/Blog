# Generated by Django 4.0.4 on 2022-07-10 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published_date_post',
            new_name='publication_date_post',
        ),
    ]