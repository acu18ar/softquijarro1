
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_cliente_options_cliente_imagen_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={
                'ordering': ['nombre'],
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.AlterField(
            model_name='cliente',
            name='imagen',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='clientes/',
                verbose_name='Imagen / Logo',
            ),
        ),
    ]
