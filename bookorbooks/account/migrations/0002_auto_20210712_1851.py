# Generated by Django 3.2.5 on 2021-07-12 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Erkek'), (2, 'Kadın'), (3, 'Other')], default=1, null=True, verbose_name='Cinsiyet'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Default'), (2, 'Çocuk'), (3, 'Ebeveyn'), (4, 'Eğitmen')], default=1, null=True, verbose_name='Hesap Türü'),
        ),
    ]