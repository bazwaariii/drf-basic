# drf-basic

Proyek REST API sederhana menggunakan **Django** dan **Django REST Framework (DRF)**.

## Fitur
- CRUD Produk (Create, Read, Update, Delete)
- Implementasi Soft Delete pada produk
- Dukungan HATEOAS links pada serializer
- Postman Collection untuk testing API

## Persyaratan
- Python 3.10+
- Pipenv atau virtualenv

## Instalasi & Menjalankan Proyek

1. **Clone repository:**
   ```bash
   git clone https://github.com/bazwaariii/drf-basic.git
   cd drf-basic
   ```

2. **Buat virtual environment dan install dependencies:**
   Menggunakan Pipenv:
   ```bash
   pipenv install
   pipenv shell
   ```
   Atau menggunakan venv standar:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/macOS:
   source venv/bin/activate

   pip install django djangorestframework
   ```

3. **Jalankan Migrasi Database:**
   ```bash
   python manage.py migrate
   ```

4. **Jalankan Server:**
   ```bash
   python manage.py runserver
   ```
   Akses API di `http://127.0.0.1:8000/`.

## Testing API
Gunakan file Postman collection yang disertakan dalam repositori:
- `[743] OpenShop API Test With Soft Delete.postman_collection.json`
- `[743] OpenShop API Test Without Soft Delete.postman_collection.json`
