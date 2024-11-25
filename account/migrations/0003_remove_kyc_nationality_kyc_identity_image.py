# Generated by Django 5.1.3 on 2024-11-25 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_ref_code_kyc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kyc',
            name='nationality',
        ),
        migrations.AddField(
            model_name='kyc',
            name='identity_image',
            field=models.ImageField(blank=True, null=True, upload_to='kyc'),
        ),
    ]