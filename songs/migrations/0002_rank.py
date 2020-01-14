# Generated by Django 3.0.2 on 2020-01-13 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0004_delete_rank'),
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('rank', models.IntegerField()),
                ('chart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='which_chart', to='charts.Chart')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='which_song', to='songs.Song')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]