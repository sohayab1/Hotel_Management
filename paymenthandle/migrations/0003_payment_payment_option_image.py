# Generated by Django 5.0.2 on 2024-04-19 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymenthandle', '0002_alter_payment_check_in_alter_payment_check_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_option_image',
            field=models.URLField(blank=True),
        ),
    ]
