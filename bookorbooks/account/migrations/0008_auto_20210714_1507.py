# Generated by Django 3.2.5 on 2021-07-14 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_childlist_child'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_child', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
        migrations.AlterField(
            model_name='parentprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_parent', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
    ]
