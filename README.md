# Django ChatApp

A clean, modern AI chat application built with **Django**, connected to **API** for LLM responses, and deployed on **Render**.

🔗 **Live Demo:**  
https://django-chatapp-mufy.onrender.com/

---

## Features

- Modern chat UI (inspired by ChatGPT & Notion)
- API LLM integration (`amazon/nova-2-lite-v1:free`)
- Secure environment variable management
- Dark/Light theme toggle
- Authentication system (login & signup)
- Production deployment using **Gunicorn + Render**
- Supports both **local installation** and **Docker deployment**

---


## Tech Stack

- **Backend:** Django, Python  
- **Frontend:** HTML, CSS, Django Templates  
- **AI Model:** OpenRouter API  
- **Deployment:** Render  
- **Server:** Gunicorn  
- **Static Files:** Whitenoise  

---

## 📦 Installation (Local - Requirements.txt)


### 1. Clone the repository
```bash
git clone https://github.com/tensormax/django-chatapp
cd django-chatapp
cd auth
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 2. Create & activate virtual environment

```bash
python3 -m venv env
source env/bin/activate    # Mac/Linux
env\Scripts\activate       # Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Create a .env file in the project root
```bash
DEBUG=True
DJANGO_SECRET=your-secret-key
OPENROUTER_KEY=your-openrouter-api-key
ALLOWED_HOSTS=127.0.0.1,localhost
```

```bash
cd auth
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

The app will be live localy at: http://127.0.0.1:8000/

### 1. Build the Docker image

```bash
docker build -t django-chatapp .
```
### 2. Run the container
```bash
docker run -p 8000:8000 \
    -e DEBUG=False \
    -e DJANGO_SECRET=your-secret-key \
    -e OPENROUTER_KEY=your-openrouter-api-key \
    -e ALLOWED_HOSTS=127.0.0.1 \
    django-chatapp
```

Your Dockerized app will be available at:
http://127.0.0.1:8000/

### Project Structure

```bash
django-chatapp/
├── auth/                     # Django project directory
├── authapp/                  # Authentication app
├── chatapp/                  # Chat UI + OpenRouter logic
├── templates/                # HTML templates
├── staticfiles/              # Static files for Render
├── utils.py                  # OpenRouter API call logic
├── requirements.txt
├── Dockerfile
├── README.md
└── manage.py


```

--------The END--------

