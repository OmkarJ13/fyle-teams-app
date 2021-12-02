# Generated by Django 3.2.9 on 2021-12-02 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_user_id', models.CharField(max_length=255, unique=True)),
                ('team_id', models.CharField(max_length=255)),
                ('team_user_conversation_reference', models.JSONField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('fyle_user_id', models.CharField(blank=True, max_length=120, null=True, unique=True)),
                ('fyle_refresh_token', models.TextField(blank=True, null=True)),
                ('fyle_org_id', models.CharField(blank=True, max_length=120, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='UserSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_type', models.CharField(max_length=120)),
                ('fyle_subscription_id', models.CharField(max_length=120, unique=True)),
                ('webhook_id', models.CharField(max_length=120, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('team_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fyle_teams_app.user', to_field='team_user_id')),
            ],
            options={
                'db_table': 'user_subscriptions',
                'unique_together': {('team_user', 'subscription_type')},
            },
        ),
    ]
