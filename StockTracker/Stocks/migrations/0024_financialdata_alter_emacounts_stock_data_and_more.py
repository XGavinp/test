# Generated by Django 5.0.1 on 2024-01-31 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stocks', '0023_remove_emacounts_ema100_count_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('close_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ema20', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ema50', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ema100', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ema200', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('rsi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('rs', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='emacounts',
            name='stock_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stocks.financialdata'),
        ),
        migrations.DeleteModel(
            name='IndicatorValues',
        ),
        migrations.DeleteModel(
            name='StockData',
        ),
    ]
