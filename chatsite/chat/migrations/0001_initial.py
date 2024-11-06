# Generated by Django 5.1.3 on 2024-11-06 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('ct_id', models.AutoField(primary_key=True, serialize=False)),
                ('ct_date', models.DateTimeField(auto_now_add=True)),
                ('ct_name', models.CharField(max_length=127)),
                ('ct_email', models.EmailField(max_length=127)),
                ('ct_subject', models.CharField(max_length=127)),
                ('ct_message', models.TextField()),
                ('ct_status', models.CharField(choices=[('received', 'Recebido'), ('readed', 'Lido'), ('responded', 'Respondido'), ('deleted', 'Apagado')], default='received', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('nw_id', models.AutoField(primary_key=True, serialize=False)),
                ('nw_date', models.DateTimeField(auto_now_add=True)),
                ('nw_author', models.CharField(blank=True, max_length=127, null=True)),
                ('nw_title', models.CharField(max_length=127)),
                ('nw_resume', models.CharField(blank=True, max_length=255, null=True)),
                ('nw_complete', models.TextField(blank=True, null=True)),
                ('nw_views', models.IntegerField(default=0)),
                ('nw_status', models.CharField(choices=[('on', 'Online'), ('off', 'Offline')], default='on', max_length=3)),
            ],
        ),
    ]
