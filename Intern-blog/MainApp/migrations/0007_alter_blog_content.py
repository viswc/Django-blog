# Generated by Django 4.1 on 2022-09-27 11:40

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_blog_readtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=10000, null=True),
        ),
    ]
