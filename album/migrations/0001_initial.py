# Generated by Django 4.0.4 on 2022-06-01 23:18

import album.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_album', models.CharField(max_length=50, verbose_name='título')),
                ('published_album', models.BooleanField(default=True, verbose_name='publicar')),
            ],
            options={
                'verbose_name_plural': 'albuns',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_image', models.CharField(blank=True, max_length=50, null=True, verbose_name='título')),
                ('image', models.ImageField(upload_to=album.models.album_direcory_path, verbose_name='imagem')),
                ('album_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.album', verbose_name='album')),
            ],
            options={
                'verbose_name': 'imagem',
                'verbose_name_plural': 'imagens',
            },
        ),
    ]