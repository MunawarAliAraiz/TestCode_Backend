# Generated by Django 4.2.4 on 2023-08-20 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_remove_question_assessment'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='question',
            constraint=models.UniqueConstraint(fields=('text', 'question_type'), name='unique_question'),
        ),
    ]
