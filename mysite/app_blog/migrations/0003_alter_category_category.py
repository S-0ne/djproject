# Generated by Django 5.2 on 2025-04-23 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_alter_article_options_alter_article_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(help_text='Максимум 250 сим.', max_length=250, verbose_name='Категорія'),
        ),
    ]
