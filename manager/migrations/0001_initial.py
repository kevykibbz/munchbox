# Generated by Django 3.2.9 on 2022-07-05 08:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import manager.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedAdmin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('main', models.BooleanField(default=False)),
                ('is_installed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'extended_admins',
                'db_table': 'extended_admin',
            },
        ),
        migrations.CreateModel(
            name='ExtendedAuthUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=13, null=True, region=None, unique=True, verbose_name='phone')),
                ('initials', models.CharField(blank=True, max_length=10, null=True)),
                ('bgcolor', models.CharField(blank=True, default=manager.models.bgcolor, max_length=10, null=True)),
                ('company', models.CharField(blank=True, default='Armlogi', max_length=100, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='placeholder.jpg', null=True, upload_to='profiles/')),
                ('role', models.CharField(blank=True, choices=[('Tertiary', 'View only'), ('Secondary', 'View | Edit'), ('Admin', 'View | Edit  | Admin')], max_length=200, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'extended_auth_users',
                'db_table': 'extended_auth_user',
                'permissions': (('can_view', 'Can view'), ('can_edit', 'Can edit'), ('can_see_invoice', 'Can see invoice')),
            },
        ),
    ]
