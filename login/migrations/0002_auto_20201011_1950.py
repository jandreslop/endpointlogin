# Generated by Django 3.1.2 on 2020-10-12 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NombreUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='login',
            name='NombreUsuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='login.nombreusuario'),
        ),
    ]
