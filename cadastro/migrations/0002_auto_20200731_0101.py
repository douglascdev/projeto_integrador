# Generated by Django 3.0.8 on 2020-07-31 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caminhao',
            old_name='hora_criacao',
            new_name='hora_cadastro',
        ),
        migrations.AddField(
            model_name='caminhao',
            name='ano',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
