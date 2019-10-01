# Generated by Django 2.2.6 on 2019-10-01 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prodes', '0004_prode_participantes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fecha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField()),
                ('prode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prodes.Prode')),
            ],
        ),
    ]
