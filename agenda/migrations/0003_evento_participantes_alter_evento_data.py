# Generated by Django 5.1.1 on 2024-09-27 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_evento_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='participantes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
    ]
