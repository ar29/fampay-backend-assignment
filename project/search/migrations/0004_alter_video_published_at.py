# Generated by Django 3.2.4 on 2021-06-21 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20210620_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='published_at',
            field=models.DateTimeField(db_index=True),
        ),
    ]
