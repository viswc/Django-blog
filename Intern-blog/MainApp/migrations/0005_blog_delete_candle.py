# Generated by Django 4.1 on 2022-09-27 11:28

import ckeditor.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_candle_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateModified', models.DateTimeField(auto_now=True)),
                ('primaryKey', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(default='BlogTitleProvider', max_length=32)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='data/media/primary/')),
                ('content', ckeditor.fields.RichTextField(blank=True, max_length=10000, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Candle',
        ),
    ]
