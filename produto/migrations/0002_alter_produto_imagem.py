# Generated by Django 4.0.3 on 2022-03-19 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='produto_Imagens/%Y/%m/'),
        ),
    ]