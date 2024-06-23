# Generated by Django 5.0.6 on 2024-06-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('color', models.CharField(default='black', max_length=100)),
                ('descriptions', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
