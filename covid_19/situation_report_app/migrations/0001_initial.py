# Generated by Django 3.0.3 on 2020-03-21 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=16, unique=True, verbose_name='название страны или места')),
                ('country', models.BooleanField(default=True, verbose_name='отметка, если страна')),
                ('notes', models.TextField(blank=True, verbose_name='примечания')),
            ],
            options={
                'verbose_name': 'страна или место',
                'verbose_name_plural': 'places',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('text', models.TextField()),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('url', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('total_cases', models.CharField(max_length=8, null=True)),
                ('new_cases', models.CharField(max_length=8, null=True)),
                ('total_deaths', models.CharField(max_length=8, null=True)),
                ('new_deaths', models.CharField(max_length=8, null=True)),
                ('total_recovered', models.CharField(max_length=8, null=True)),
                ('country_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='situation_report_app.Place')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('name', models.CharField(max_length=32)),
                ('url', models.CharField(max_length=64)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='situation_report_app.Source')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
