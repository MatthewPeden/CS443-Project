# Generated by Django 4.1.3 on 2022-11-20 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='BeefCowGroup',
        ),
        migrations.DeleteModel(
            name='BeefCowGroupIngredients',
        ),
        migrations.DeleteModel(
            name='ChickenGroup',
        ),
        migrations.DeleteModel(
            name='ChickenGroupIngredients',
        ),
        migrations.DeleteModel(
            name='DairyCowGroup',
        ),
        migrations.DeleteModel(
            name='DairyCowGroupIngredients',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='FeedBatch',
        ),
        migrations.DeleteModel(
            name='GoatGroup',
        ),
        migrations.DeleteModel(
            name='GoatGroupIngredients',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='PigGroup',
        ),
        migrations.DeleteModel(
            name='PigGroupIngredients',
        ),
    ]