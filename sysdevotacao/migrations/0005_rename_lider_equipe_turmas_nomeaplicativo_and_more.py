# Generated by Django 4.2.6 on 2023-11-10 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sysdevotacao', '0004_rename_link_aplicativo_turmas_linkyoutube'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turmas',
            old_name='lider_equipe',
            new_name='nomeAplicativo',
        ),
        migrations.RenameField(
            model_name='turmas',
            old_name='nome_aplicativo',
            new_name='nomeEquipe',
        ),
        migrations.RemoveField(
            model_name='turmas',
            name='arquivo_aplicativo',
        ),
        migrations.RemoveField(
            model_name='turmas',
            name='email',
        ),
        migrations.RemoveField(
            model_name='turmas',
            name='integrantes',
        ),
        migrations.RemoveField(
            model_name='turmas',
            name='nome_equipe',
        ),
        migrations.RemoveField(
            model_name='turmas',
            name='tutor',
        ),
    ]