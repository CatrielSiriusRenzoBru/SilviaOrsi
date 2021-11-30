# Generated by Django 3.2.9 on 2021-11-06 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Setup', '0003_staff'),
        ('Depilacion', '0003_alter_depilacion_foto_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depilacion_staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Observacion', models.TextField(blank=True, max_length=140, null=True)),
                ('Depilacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Depilacion.depilacion')),
                ('asistente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Setup.staff')),
            ],
            options={
                'verbose_name': 'Asistente',
                'verbose_name_plural': 'Asistente',
            },
        ),
    ]