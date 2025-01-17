# Generated by Django 2.1 on 2020-02-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailGun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.EmailField(blank=True, max_length=254, null=True)),
                ('sender', models.EmailField(blank=True, max_length=254, null=True)),
                ('_from', models.EmailField(blank=True, max_length=254, null=True)),
                ('subject', models.CharField(blank=True, max_length=256, null=True)),
                ('body_plain', models.TextField(blank=True, null=True)),
                ('stripped_text', models.TextField(blank=True, null=True)),
                ('stripped_signature', models.TextField(blank=True, null=True)),
                ('body_html', models.TextField(blank=True, null=True)),
                ('stripped_html', models.TextField(blank=True, null=True)),
                ('attachment_count', models.IntegerField(blank=True, null=True)),
                ('attachment_x', models.TextField(blank=True, null=True)),
                ('timestamp', models.IntegerField(blank=True, null=True)),
                ('token', models.TextField(blank=True, null=True)),
                ('signature', models.TextField(blank=True, null=True)),
                ('message_headers', models.TextField(blank=True, null=True)),
                ('content_id_map', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
