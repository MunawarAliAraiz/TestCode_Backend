# Generated by Django 4.2.4 on 2023-08-20 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0010_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='selected_choice_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
