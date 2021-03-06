# Generated by Django 3.0.2 on 2020-01-07 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200107_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='descricao',
            field=models.TextField(max_length=200, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-stats-up', 'Gráfico'), ('lni-users', 'Usuários'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete')], max_length=12, verbose_name='Serviço'),
        ),
    ]
