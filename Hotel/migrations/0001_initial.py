# Generated by Django 4.0.6 on 2022-08-21 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField(null=True)),
                ('check_out', models.DateField(null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('region', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('Specificlocation_or_subcity', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('star', models.PositiveIntegerField()),
                ('number_of_room', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Hotel.city')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('service_number', models.CharField(max_length=255)),
                ('payment_step', models.TextField()),
                ('customer_service', models.PositiveIntegerField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkWithUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('hotel_name', models.CharField(max_length=255)),
                ('hotel_address', models.CharField(max_length=255)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookingRoomNumber',
            fields=[
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='booking_roomnumber', serialize=False, to='Hotel.booking')),
                ('room_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookingStatus',
            fields=[
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='booking_status', serialize=False, to='Hotel.booking')),
                ('accept', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FinishPayment',
            fields=[
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='finishpymnt_booking', serialize=False, to='Hotel.booking')),
                ('paid_by', models.CharField(max_length=255, null=True)),
                ('transactionid', models.CharField(max_length=255, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('room_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('facility', models.CharField(max_length=200)),
                ('number_of_bed', models.PositiveIntegerField()),
                ('max_people', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInformations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=255)),
                ('service_number', models.CharField(max_length=255)),
                ('account_or_shortcode', models.PositiveIntegerField()),
                ('account_or_shortcode_holder', models.CharField(max_length=255)),
                ('phone_number', models.PositiveIntegerField()),
                ('customer_service', models.PositiveIntegerField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='HotelAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_admin', to='Hotel.hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('hotel', models.ManyToManyField(to='Hotel.hotel')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Hotel.hotel'),
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Hotel.roomgroup'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='FnishPaymentStatus',
            fields=[
                ('fnishpayment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='finishpayment_status', serialize=False, to='Hotel.finishpayment')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='finishpayment',
            name='payment_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel.paymentinformations'),
        ),
    ]
