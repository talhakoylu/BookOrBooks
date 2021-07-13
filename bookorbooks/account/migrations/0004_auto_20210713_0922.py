# Generated by Django 3.2.5 on 2021-07-13 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_customuser_identity_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Erkek'), (2, 'Kadın'), (3, 'Other')], default=1, verbose_name='Cinsiyet'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Default'), (2, 'Çocuk'), (3, 'Ebeveyn'), (4, 'Eğitmen')], default=1, verbose_name='Hesap Türü'),
        ),
    ]
