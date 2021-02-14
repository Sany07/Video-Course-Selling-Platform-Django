# Generated by Django 3.0.8 on 2021-02-11 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_auto_20210211_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizexam',
            name='quiz',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='quiz_exam', to='quizapp.Quiz'),
            preserve_default=False,
        ),
    ]
