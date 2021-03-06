# Generated by Django 4.0.4 on 2022-07-22 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReportRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reports_userreportregister', models.PositiveIntegerField(default=0, verbose_name='denúncias')),
                ('status_userreportregister', models.CharField(choices=[('n', 'Normal'), ('b', 'Bloqueado')], default='n', max_length=1, verbose_name='situação')),
                ('user_userreportregister', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuário')),
            ],
            options={
                'verbose_name': 'denúncias dos usuários',
            },
        ),
    ]
