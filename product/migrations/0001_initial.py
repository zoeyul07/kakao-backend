# Generated by Django 3.0.5 on 2020-05-01 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=2000)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'characters',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'colors',
            },
        ),
        migrations.CreateModel(
            name='HotImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=2000)),
            ],
            options={
                'db_table': 'hot_images',
            },
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('image_url', models.URLField(max_length=2000)),
            ],
            options={
                'db_table': 'main_categories',
            },
        ),
        migrations.CreateModel(
            name='NewImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image_url', models.URLField(max_length=2000)),
                ('description', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'new_images',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('detail', models.TextField()),
                ('sub_detail', models.TextField()),
                ('stock', models.IntegerField(default=0)),
                ('image_url', models.URLField(max_length=2000)),
                ('created_at', models.DateTimeField()),
                ('global_delivery', models.BooleanField(default=1)),
                ('sales_quantity', models.IntegerField(default=0)),
                ('discount', models.BooleanField(default=1)),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('account_product_basket', models.ManyToManyField(through='order.Basket', to='account.Account')),
                ('hot_image', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.HotImage')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
            ],
            options={
                'db_table': 'products_sizes',
            },
        ),
        migrations.CreateModel(
            name='ProductTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
            ],
            options={
                'db_table': 'products_themes',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('account_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Account')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='SeriesCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image_url', models.URLField(max_length=2000)),
            ],
            options={
                'db_table': 'series_categories',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('main_image_url', models.URLField(max_length=2000)),
                ('detail_image_url', models.URLField(max_length=2000)),
                ('description', models.CharField(max_length=1000)),
                ('product_theme', models.ManyToManyField(through='product.ProductTheme', to='product.Product')),
            ],
            options={
                'db_table': 'themes',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('main_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.MainCategory')),
            ],
            options={
                'db_table': 'sub_categories',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('product_size', models.ManyToManyField(through='product.ProductSize', to='product.Product')),
            ],
            options={
                'db_table': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='ReviewLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Account')),
                ('review', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Review')),
            ],
            options={
                'db_table': 'review_likes',
            },
        ),
        migrations.AddField(
            model_name='producttheme',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Theme'),
        ),
        migrations.AddField(
            model_name='productsize',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Size'),
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
            ],
            options={
                'db_table': 'products_orders',
            },
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Color')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
            ],
            options={
                'db_table': 'products_colors',
            },
        ),
        migrations.CreateModel(
            name='ProductCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Character')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
            ],
            options={
                'db_table': 'products_characters',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.MainCategory')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.SubCategory')),
            ],
            options={
                'db_table': 'products_categories',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='maincategory_product',
            field=models.ManyToManyField(through='product.ProductCategory', to='product.MainCategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='series_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.SeriesCategory'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=2000)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
                ('theme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Theme')),
            ],
            options={
                'db_table': 'homes',
            },
        ),
        migrations.AddField(
            model_name='color',
            name='product_color',
            field=models.ManyToManyField(through='product.ProductColor', to='product.Product'),
        ),
        migrations.AddField(
            model_name='character',
            name='product_character',
            field=models.ManyToManyField(through='product.ProductCharacter', to='product.Product'),
        ),
    ]
