# Generated by Django 3.0.8 on 2020-09-07 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='photos/quiz/%Y-%m-%d/')),
                ('choice_one', models.CharField(max_length=250)),
                ('choice_two', models.CharField(max_length=250)),
                ('choice_three', models.CharField(max_length=250)),
                ('choice_four', models.CharField(max_length=250)),
                ('ans', models.CharField(choices=[('choice_one', 'One'), ('choice_two', 'Two'), ('choice_three', 'Three'), ('choice_four', 'Four')], max_length=300)),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
            },
        ),
    ]
