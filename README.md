# davaleba46_p

Simple Django project for uploading and displaying images/files.

## Features
- `Category` and `Photo` models.
- `ImageField` + `FileField` with custom validators from `utils/validators.py`.
- Media configuration with `MEDIA_URL` and `MEDIA_ROOT`.
- Browser page that renders uploaded images and file URLs.
- Optional AWS S3 integration using `django-storages` and `boto3`.

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Optional AWS S3
Set env variables and enable S3:
```bash
export USE_S3=True
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
export AWS_STORAGE_BUCKET_NAME=...
export AWS_S3_REGION_NAME=eu-central-1
```
