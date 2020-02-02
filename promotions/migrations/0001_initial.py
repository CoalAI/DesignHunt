# Generated by Django 2.1 on 2020-01-23 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=256, verbose_name='Company name')),
                ('company_domain', models.CharField(max_length=256, verbose_name='Company Domain')),
                ('email_from', models.EmailField(blank=True, max_length=256, null=True, verbose_name='Email From')),
                ('email_to', models.EmailField(blank=True, max_length=256, null=True, verbose_name='Email To')),
                ('promotion_heading', models.CharField(max_length=256, verbose_name='Promotion Subject')),
                ('promotion_url', models.URLField(blank=True, null=True)),
                ('promotion_type', models.CharField(max_length=100, verbose_name='Promotion Type')),
                ('content', models.TextField(verbose_name='HTML Email')),
                ('email_mobile', models.URLField(blank=True, null=True)),
                ('email_desktop', models.URLField(blank=True, null=True)),
                ('techknowlogy', models.CharField(blank=True, max_length=64, null=True, verbose_name='Email powered by')),
                ('medium', models.CharField(choices=[('MEDIUM_FB', 'Facebook'), ('MEDIUM_EMAIL', 'Email')], default='MEDIUM_FB', max_length=64, verbose_name='Medium')),
                ('recieved_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
