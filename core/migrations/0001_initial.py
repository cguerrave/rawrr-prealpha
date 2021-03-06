# Generated by Django 2.0.7 on 2018-07-25 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImplementationTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('order', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=140)),
                ('description', models.TextField(blank=True)),
                ('needed_staff', models.TextField(blank=True)),
                ('estimated_money_investment', models.TextField(blank=True)),
                ('how_to_get_help', models.TextField(blank=True)),
                ('max_risk_level', models.FloatField(blank=True, null=True)),
                ('highlight', models.BooleanField(default=False)),
                ('priorization', models.FloatField(blank=True, null=True)),
                ('implementation_term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ImplementationTerm')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('description', models.TextField(blank=True)),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Organization')),
                ('recommendations_associated', models.ManyToManyField(blank=True, to='core.Recommendation')),
            ],
        ),
        migrations.CreateModel(
            name='SecurityField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('color', models.CharField(max_length=7)),
                ('description', models.TextField(blank=True)),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=140)),
                ('description', models.TextField(blank=True)),
                ('impact', models.IntegerField(blank=True)),
                ('likelihood', models.IntegerField(blank=True)),
                ('risk_level', models.FloatField(blank=True)),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Organization')),
                ('security_field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.SecurityField')),
            ],
        ),
        migrations.CreateModel(
            name='Vulnerability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=140)),
                ('description', models.TextField(blank=True)),
                ('references', models.TextField(blank=True)),
                ('other_info', models.TextField(blank=True)),
                ('max_risk_level', models.FloatField(blank=True, null=True)),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Organization')),
                ('threats_associated', models.ManyToManyField(blank=True, to='core.Threat')),
            ],
        ),
        migrations.AddField(
            model_name='recommendation',
            name='vulnerabilities_associated',
            field=models.ManyToManyField(blank=True, to='core.Vulnerability'),
        ),
    ]
