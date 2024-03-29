# Generated by Django 3.2.5 on 2021-07-29 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_takingquiz_takingquizanswer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='takingquizanswer',
            options={'verbose_name': 'Çözülmüş Sınav Cevabı', 'verbose_name_plural': 'Çözülmüş Sınav Cevapları'},
        ),
        migrations.AlterField(
            model_name='takingquizanswer',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='answer_taking_quiz', to='quiz.answer', verbose_name='Cevap'),
        ),
    ]
