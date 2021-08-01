# Generated by Django 3.2.5 on 2021-07-29 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0003_readinghistory_counter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('title', models.CharField(max_length=150, verbose_name='Başlık')),
                ('enabled', models.BooleanField(choices=[(True, 'Aktif'), (False, 'Aktif Değil')], default=False, verbose_name='Sınav Aktif Mi?')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_quiz', to='book.book', verbose_name='Kitap')),
            ],
            options={
                'verbose_name': 'Sınavlar',
                'verbose_name_plural': 'Sınav',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('question', models.CharField(max_length=500, verbose_name='Soru')),
                ('topic', models.CharField(help_text='Rapor sayfasında, cevabın yanlış olması durumunda gösterilecek metin.', max_length=500, verbose_name='Konu')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='question_quiz', to='quiz.quiz', verbose_name='Sınav')),
            ],
            options={
                'verbose_name': 'Soru',
                'verbose_name_plural': 'Sorular',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('answer', models.CharField(max_length=500, verbose_name='Cevap')),
                ('is_correct', models.BooleanField(choices=[(True, 'Doğru Cevap'), (False, 'Yanlış Cevap')], default=False, verbose_name='Doğru Bir Cevap Mı?')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_answer', to='quiz.question', verbose_name='Soru')),
            ],
            options={
                'verbose_name': 'Cevap',
                'verbose_name_plural': 'Cevaplar',
            },
        ),
    ]
