# Generated by Django 5.0.1 on 2024-01-30 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stocks', '0022_remove_emacounts_ema100_prev_state_positive_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emacounts',
            name='ema100_count',
        ),
        migrations.RemoveField(
            model_name='emacounts',
            name='ema200_count',
        ),
        migrations.RemoveField(
            model_name='emacounts',
            name='ema20_count',
        ),
        migrations.RemoveField(
            model_name='emacounts',
            name='ema50_count',
        ),
        migrations.AddField(
            model_name='emacounts',
            name='ema100_output',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='emacounts',
            name='ema200_output',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='emacounts',
            name='ema20_output',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='emacounts',
            name='ema50_output',
            field=models.TextField(blank=True),
        ),
    ]