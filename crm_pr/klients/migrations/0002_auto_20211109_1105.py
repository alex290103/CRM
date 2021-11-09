# Generated by Django 3.2.8 on 2021-11-09 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('klients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Istochnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('istochnik', models.TextField(max_length=30)),
            ],
            options={
                'verbose_name': 'Источник',
                'verbose_name_plural': 'Источники',
            },
        ),
        migrations.CreateModel(
            name='StatusKlienta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField(max_length=30)),
            ],
            options={
                'verbose_name': 'Статус клиента',
                'verbose_name_plural': 'Статус клиента',
            },
        ),
        migrations.RemoveField(
            model_name='klients',
            name='status_klienta',
        ),
        migrations.AlterField(
            model_name='klients',
            name='istochnik',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='klienty', to='klients.istochnik'),
        ),
        migrations.AlterField(
            model_name='klients',
            name='servise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='klienty', to='klients.statusklienta'),
        ),
    ]
