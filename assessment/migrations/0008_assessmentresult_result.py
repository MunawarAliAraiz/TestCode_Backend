# Generated by Django 4.2.4 on 2023-08-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0007_remove_assessmentresult_unique_assessment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessmentresult',
            name='result',
            field=models.JSONField(null=True),
        ),
    ]