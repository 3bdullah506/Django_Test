# ════════════════════════════════════════════════════════
#  settings.py — إعدادات المشروع
# ════════════════════════════════════════════════════════

from pathlib import Path

# مسار المجلد الرئيسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح سري — لا تشاركه مع أحد في المشاريع الحقيقية
SECRET_KEY = 'django-secret-key-2024'

# وضع التطوير — اجعله False عند النشر
DEBUG = True

ALLOWED_HOSTS = ['*']

# ─── التطبيقات المثبتة في المشروع ───────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',          # لوحة الإدارة
    'django.contrib.auth',           # نظام المستخدمين
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    # الملفات الثابتة (CSS, صور)
    'rest_framework', 
    'corsheaders',               # ← Topic 10: Django REST Framework
    'delivery',                      # ← تطبيقنا
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
    ]},
}]

WSGI_APPLICATION = 'mysite.wsgi.application'

# ─── قاعدة البيانات ──────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # ملف واحد بسيط
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []

# ─── اللغة والتوقيت ──────────────────────────────────────
LANGUAGE_CODE = 'ar'
TIME_ZONE     = 'Asia/Aden'
USE_I18N      = True
USE_TZ        = True

# ─── Topic 3: الملفات الثابتة (CSS, صور) ─────────────────
STATIC_URL = '/static/'

# ─── بعد تسجيل الدخول يذهب لقائمة الطلبات ──────────────
LOGIN_REDIRECT_URL = '/'
# بعد الخروج يذهب لصفحة الدخول
LOGOUT_REDIRECT_URL = '/login/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



CORS_ALLOW_ALL_ORIGINS = True