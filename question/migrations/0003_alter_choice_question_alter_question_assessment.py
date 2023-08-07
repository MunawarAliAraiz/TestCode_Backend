# Generated by Django 4.2.4 on 2023-08-07 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0003_alter_assessment_title'),
        ('question', '0002_alter_testcase_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='question.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='assessment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='assessment.assessment'),
        ),
    ]
