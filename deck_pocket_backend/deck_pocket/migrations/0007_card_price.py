# Generated by Django 3.0.5 on 2020-05-03 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deck_pocket', '0006_mycards_whishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True),
        ),
    ]
