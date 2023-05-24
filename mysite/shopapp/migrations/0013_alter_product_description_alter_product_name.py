# Generated by Django 4.1.5 on 2023-05-24 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0012_alter_order_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, db_index=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='name'),
        ),
    ]
