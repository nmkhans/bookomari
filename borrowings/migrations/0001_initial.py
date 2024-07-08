# Generated by Django 5.0.6 on 2024-07-08 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_alter_useraccount_account_id_and_more'),
        ('books', '0002_book_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowing_price', models.IntegerField()),
                ('balance_after_borrowing', models.IntegerField()),
                ('borrowing_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('borrowed', 'Borrowed'), ('returned', 'Returned')], max_length=100)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowings', to='accounts.useraccount')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowings', to='books.book')),
            ],
        ),
    ]
