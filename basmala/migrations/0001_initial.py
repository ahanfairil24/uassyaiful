# Generated by Django 4.1.2 on 2022-12-31 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='basmala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ketua', models.CharField(max_length=100)),
                ('sekretaris', models.CharField(max_length=50)),
                ('bendahara', models.CharField(max_length=50)),
                ('divisi', models.IntegerField(null=True)),
            ],
        ),
    ]
