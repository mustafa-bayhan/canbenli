# Generated by Django 4.2.4 on 2023-08-05 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('can', '0009_post_summary_en_post_summary_tr'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='read_en',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='read_tr',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
