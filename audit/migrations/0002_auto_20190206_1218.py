# Generated by Django 2.1.5 on 2019-02-06 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='conflict',
            field=models.CharField(blank=True, choices=[('none', 'Ninguno'), ('observation', 'Observación'), ('find', 'Hallazgo')], max_length=10, null=True),
        ),
    ]