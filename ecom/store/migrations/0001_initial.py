# Generated by Django 3.2.7 on 2021-10-12 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.PositiveIntegerField()),
                ('quantity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=2054)),
                ('qty_lct', models.FloatField()),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store')),
            ],
        ),
    ]
