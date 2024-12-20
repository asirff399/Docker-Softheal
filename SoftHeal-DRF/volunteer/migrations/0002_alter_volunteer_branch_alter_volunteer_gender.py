# Generated by Django 5.1 on 2024-09-05 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='branch',
            field=models.CharField(choices=[('Rajshahi', 'Rajshahi'), ('Rangpur', 'Rangpur'), ('Mymensingh', 'Mymensingh'), ('Khulna', 'Khulna'), ('Dhaka', 'Dhaka'), ('Barisal', 'Barisal'), ('Sylhet', 'Sylhet'), ('Chittagong', 'Chittagong')], default='Rajshahi', max_length=30),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=30),
        ),
    ]
