# Generated by Django 3.2.9 on 2022-07-11 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0021_auto_20220711_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanmodel',
            name='tenature',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]