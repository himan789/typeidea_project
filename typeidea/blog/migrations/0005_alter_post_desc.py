# Generated by Django 4.1.3 on 2023-01-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.CharField(blank=True, max_length=1024, verbose_name='摘要'),
        ),
    ]
