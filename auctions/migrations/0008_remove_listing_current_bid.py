from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_bid_bidder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='current_bid',
        ),
    ]
