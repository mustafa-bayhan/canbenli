# Generated by Django 4.1.2 on 2023-04-01 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('can', '0003_alter_comment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
