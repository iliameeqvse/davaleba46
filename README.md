
- `Category` and `Photo` models.
- `ImageField` + `FileField` with custom validators from `utils/validators.py`.
- Media configuration with `MEDIA_URL` and `MEDIA_ROOT`.
- Browser page that renders uploaded images and file URLs.

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
