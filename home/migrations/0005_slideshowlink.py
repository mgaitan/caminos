# Generated by Django 2.1.8 on 2019-04-16 22:31

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0004_auto_20190413_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideshowLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('text', models.CharField(blank=True, max_length=255, null=True)),
                ('button_text', models.CharField(blank=True, max_length=255, null=True)),
                ('home_page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='slideshow_links', to='home.HomePage')),
                ('image', models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Page')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
