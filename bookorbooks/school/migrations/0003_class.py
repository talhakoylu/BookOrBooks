# Generated by Django 3.2.5 on 2021-07-19 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_instructorprofile'),
        ('school', '0002_alter_school_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('name', models.CharField(max_length=50, verbose_name='Sınıf Adı')),
                ('grade', models.IntegerField(verbose_name='Sınıf Derecesi')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructors_school', to='account.instructorprofile', verbose_name='Eğitmen')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes_school', to='school.school', verbose_name='Okul')),
            ],
            options={
                'verbose_name': 'Sınıf',
                'verbose_name_plural': 'Sınıflar',
            },
        ),
    ]