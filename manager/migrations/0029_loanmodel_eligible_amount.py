# Generated by Django 3.2.9 on 2022-07-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0028_loanmodel_card_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanmodel',
            name='eligible_amount',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]