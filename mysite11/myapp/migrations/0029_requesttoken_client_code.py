# Generated by Django 2.2.4 on 2019-11-24 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_requesttoken_whlist_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='requesttoken',
            name='Client_code',
            field=models.CharField(max_length=6, null=True),
        ),
    ]