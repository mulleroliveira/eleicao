# Generated by Django 2.2.2 on 2019-06-27 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cpf',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
    ]
