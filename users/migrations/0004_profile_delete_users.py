# Generated by Django 4.1.3 on 2022-11-20 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_alter_users_family_alter_users_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('has_a_family', models.BooleanField(default=False)),
                ('is_head', models.BooleanField(default=False)),
                ('position', models.CharField(blank=True, choices=[('0', 'Father'), ('1', 'Mother'), ('2', 'Son'), ('3', 'Daughter'), ('4', 'Sister'), ('5', 'Brother'), ('6', 'Husband'), ('7', 'Wife')], max_length=1, null=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.family')),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
