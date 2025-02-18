# Generated by Django 5.1 on 2024-08-30 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='description',
        ),
        migrations.RemoveField(
            model_name='order',
            name='stripe_pyment_intent_id',
        ),
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(default='USD', max_length=3),
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='api_app.item'),
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
