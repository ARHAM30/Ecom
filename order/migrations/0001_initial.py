# Generated by Django 2.2.4 on 2020-07-25 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0007_auto_20200725_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_all',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=50, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Contact', models.IntegerField(blank=True, null=True)),
                ('Address1', models.CharField(max_length=120)),
                ('Address2', models.CharField(blank=True, max_length=120, null=True)),
                ('City', models.CharField(max_length=25)),
                ('status', models.CharField(choices=[('success', 'success'), ('fail', 'fail'), ('initial', 'initial')], default='initial', max_length=100)),
                ('State', models.CharField(max_length=25)),
                ('Pincode', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Products')),
            ],
        ),
    ]
