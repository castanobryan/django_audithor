# Generated by Django 2.1.5 on 2019-02-06 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auditor_name', models.CharField(max_length=50)),
                ('audited_name', models.CharField(max_length=50)),
                ('audited_job', models.CharField(max_length=255)),
                ('process_to_be_audited', models.CharField(max_length=100)),
                ('audit_scope', models.CharField(max_length=255)),
                ('audited_phone_number', models.CharField(max_length=15)),
                ('date', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Numeral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeral', models.CharField(max_length=8)),
                ('title', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('method', models.TextField(blank=True, max_length=255, null=True)),
                ('conflict', models.CharField(choices=[('none', 'Ninguno'), ('observation', 'Observación'), ('find', 'Hallazgo')], max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('numeral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.Numeral')),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('audit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='audit.Audit')),
            ],
        ),
        migrations.AddField(
            model_name='numeral',
            name='rule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.Rule'),
        ),
    ]
