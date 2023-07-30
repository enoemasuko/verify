# Generated by Django 4.2.3 on 2023-07-27 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company_name', models.CharField(max_length=50)),
                ('date_of_registration', models.CharField(max_length=50)),
                ('company_registration_number', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('contact_person', models.CharField(max_length=50)),
                ('list_of_departments', models.CharField(max_length=50)),
                ('number_of_emlpoyees', models.CharField(max_length=50)),
                ('contact_phone', models.CharField(max_length=50)),
                ('email_address', models.CharField(max_length=50)),
                ('name_of_employee', models.CharField(max_length=50)),
                ('employee_id', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('date_started', models.CharField(max_length=50)),
                ('date_left_role', models.CharField(max_length=50)),
                ('duties', models.CharField(max_length=50)),
            ],
        ),
    ]