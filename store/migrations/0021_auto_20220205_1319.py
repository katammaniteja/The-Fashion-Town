# Generated by Django 3.2.9 on 2022-02-05 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_alter_cart_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='wishlist',
            options={'ordering': ['-created_at']},
        ),
    ]
