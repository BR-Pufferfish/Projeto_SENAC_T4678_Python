import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf_cnpj', models.CharField(max_length=14)),
                ('razao_social', models.CharField(max_length=100)),
                ('data_nascimento', models.DateTimeField()),
                ('contato', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=100)),
                ('tipo_pessoa', models.CharField(choices=[('Cliente', 'Cliente'), ('Colaborador', 'Colaborador')], default='Cliente', max_length=20)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mercadoria', models.CharField(max_length=100)),
                ('data_entrada', models.DateTimeField(auto_now_add=True)),
                ('origem', models.CharField(max_length=100)),
                ('saldo', models.IntegerField()),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.categoria')),
                ('pessoa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Movimentacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('dtSaida', models.DateTimeField(auto_now_add=True)),
                ('destino', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Transportando', 'Transportando'), ('Entregue', 'Entregue')], default='Transportando', max_length=20)),
                ('estoque', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.estoque')),
                ('pessoa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.pessoa')),
            ],
        ),
    ]
