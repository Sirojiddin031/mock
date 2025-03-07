# Generated by Django 4.2.6 on 2023-10-25 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configApp', '0003_remove_group_worker'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('descriptions', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='group',
            name='day',
        ),
        migrations.RemoveField(
            model_name='group',
            name='room',
        ),
        migrations.AlterField(
            model_name='group',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('descriptions', models.CharField(blank=True, max_length=500, null=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='configApp.rooms')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='configApp.tabletype')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='table',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='configApp.table'),
            preserve_default=False,
        ),
    ]
