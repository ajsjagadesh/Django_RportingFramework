# Generated by Django 4.2.5 on 2023-10-10 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Custom_Report_Config',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('report_name', models.CharField(max_length=200)),
                ('input_page', models.JSONField()),
                ('server_query', models.JSONField()),
                ('output_page', models.JSONField()),
            ],
            options={
                'db_table': 'custom_report_config',
            },
        ),
    ]
