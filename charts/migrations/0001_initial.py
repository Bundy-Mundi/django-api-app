# Generated by Django 3.0.2 on 2020-01-13 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('charts', models.ManyToManyField(related_name='charts', to='charts.Chart')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('chart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='which_chart', to='charts.Chart')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='chart',
            name='songs',
            field=models.ManyToManyField(related_name='songs', to='charts.Song'),
        ),
    ]