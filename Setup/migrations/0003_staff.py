# Generated by Django 3.2.9 on 2021-11-06 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Setup', '0002_alter_clientes_observacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asistente', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staff',
            },
        ),
    ]