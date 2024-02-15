# Generated by Django 5.0.2 on 2024-02-13 19:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title_en', models.CharField(blank=True, max_length=256, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=256, null=True)),
                ('img', models.FileField(upload_to='country/')),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title_en', models.CharField(blank=True, max_length=256, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=256, null=True)),
                ('img', models.FileField(upload_to='country/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]