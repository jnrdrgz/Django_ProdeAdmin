# Generated by Django 2.2.6 on 2019-10-01 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodes', '0003_remove_prode_participantes'),
    ]

    operations = [
        migrations.AddField(
            model_name='prode',
            name='participantes',
            field=models.ManyToManyField(to='prodes.Participante'),
        ),
    ]
