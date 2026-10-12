"""
Configuración del proyecto SoftQuijarro S.R.L.

⚠️  ARCHIVO DEL DOCENTE. Los estudiantes NO lo modifican.
    Si necesitas algo aquí (una librería nueva, una configuración), pídelo
    abriendo un Issue en GitHub. La verificación automática rechaza los
    pull requests que tocan este archivo.
"""
import os
from pathlib import Path

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# En Render existe la variable RENDER; en Codespaces o en tu PC, no.
EN_PRODUCCION = "RENDER" in os.environ

SECRET_KEY = os.environ.get(
    "SECRET_KEY", "solo-para-desarrollo-no-usar-en-produccion-softquijarro"
)
DEBUG = not EN_PRODUCCION

if EN_PRODUCCION:
    ALLOWED_HOSTS = []
    host = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
    if host:
        ALLOWED_HOSTS.append(host)
else:
    ALLOWED_HOSTS = ["*"]

# Codespaces publica la app en *.app.github.dev y Render en *.onrender.com
CSRF_TRUSTED_ORIGINS = ["https://*.app.github.dev", "https://*.onrender.com"]

# ---------------------------------------------------------------------------
# Las 5 apps de los estudiantes ya están registradas. Nadie necesita tocar
# esta lista: cada uno trabaja dentro de su propia carpeta.
# ---------------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Base común (docente)
    "core",
    # Módulos de los estudiantes
    "clientes",
    "productos",
    "facturacion",
    "proveedores",
    "reportes",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "core.middleware.LoginObligatorioMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core.context_processors.menu_modulos",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# ---------------------------------------------------------------------------
# Base de datos
#   - En Codespaces / tu PC: SQLite, una base propia de cada estudiante.
#   - En Render: PostgreSQL, la única base compartida (la de la demo).
# ---------------------------------------------------------------------------
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
]

LANGUAGE_CODE = "es"
TIME_ZONE = "America/La_Paz"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {
        "BACKEND": (
            "whitenoise.storage.CompressedManifestStaticFilesStorage"
            if EN_PRODUCCION
            else "django.contrib.staticfiles.storage.StaticFilesStorage"
        )
    },
}

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "inicio"
LOGOUT_REDIRECT_URL = "login"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

if EN_PRODUCCION:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
