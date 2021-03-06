# Generated by Django 3.2.8 on 2021-11-16 03:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('thumbnail', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('body', models.TextField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('thumbnail', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('demo_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('source_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('tags', models.ManyToManyField(blank=True, to='base.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('author', models.CharField(default='Tyrone', editable=False, max_length=100)),
                ('sub_title', models.CharField(blank=True, max_length=255, null=True)),
                ('thumbnail', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('body', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('tags', models.ManyToManyField(blank=True, to='base.Tag')),
            ],
        ),
    ]
