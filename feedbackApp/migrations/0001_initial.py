# Generated by Django 4.1.6 on 2023-02-21 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_date', models.DateTimeField(auto_now_add=True)),
                ('feedback_content', models.TextField(default='글을 작성해주세요.')),
            ],
        ),
    ]
