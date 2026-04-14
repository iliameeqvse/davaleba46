from django.db import migrations, models
import django.db.models.deletion

import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='photos/images/', validators=[utils.validators.validate_image_size, utils.validators.validate_image_extension])),
                ('file', models.FileField(blank=True, null=True, upload_to='photos/files/', validators=[utils.validators.validate_file_size, utils.validators.validate_file_extension])),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='gallery.category')),
            ],
        ),
    ]
