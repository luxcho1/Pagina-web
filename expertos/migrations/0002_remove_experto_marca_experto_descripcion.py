# Generated by Django 4.0.5 on 2022-07-11 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expertos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experto',
            name='marca',
        ),
        migrations.AddField(
            model_name='experto',
            name='descripcion',
            field=models.CharField(default=1, max_length=500, verbose_name='Descripcion'),
            preserve_default=False,
        ),
    ]