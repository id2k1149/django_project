# Generated by Django 3.0.3 on 2020-02-28 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('situation_report', '0005_auto_20200228_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('text', models.TextField()),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Information',
        ),
    ]