from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_listing_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image_link',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
