# Generated by Django 4.2.17 on 2024-12-15 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='published',
        ),
    ]