##Django ChatApp

A modern, clean, real-time styled chat interface built using Django, designed with a UI inspired by Notion, ChatGPT, and Flow AI.
This project is production-ready and deployed on Render.

🚀 Features

🔐 User Authentication (Login & Signup)

💬 Clean, minimalistic chat UI

🌗 Light/Dark Theme Toggle

⚡ Fast and optimized Django backend

🐳 Docker support for easy deployment

🔧 Fully environment-variable driven configuration

🗄️ Gunicorn for production

🏗️ Tech Stack

Backend: Django, Python

Frontend: HTML, CSS, JS

Production Server: Gunicorn

Hosting: Render

Containerization: Docker

🔧 Environment Variables

Create a .env file (never commit this to GitHub):

DEBUG=False
DJANGO_SECRET=your-secret-key
ALLOWED_HOSTS=your-render-url,localhost,127.0.0.1


In Render → Environment → Add these exact keys.


⚙️ Local Installation (without Docker)
1️⃣ Clone Repo
git clone https://github.com/tensormax/django-chatapp
cd django-chatapp

2️⃣ Create Virtual Environment
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Environment Variables

Create .env file:

DEBUG=True
DJANGO_SECRET=your-secret
ALLOWED_HOSTS=localhost,127.0.0.1

5️⃣ Run Migrations
python manage.py migrate

6️⃣ Start Development Server
python manage.py runserver


App will be available at:
👉 http://127.0.0.1:8000/

🐳 Run Using Docker (Recommended)
1️⃣ Build the Docker Image
docker build -t django-chatapp .

2️⃣ Run the Container
docker run -p 8000:8000 \
  -e DEBUG=False \
  -e DJANGO_SECRET=your-secret-key \
  -e ALLOWED_HOSTS=localhost,127.0.0.1 \
  django-chatapp


The app will be available at:
👉 http://localhost:8000/

3️⃣ Pull Image (If Pushed to Docker Hub)
docker pull your-username/django-chatapp
docker run -p 8000:8000 your-username/django-chatapp

🚀 Deployment (Render)

Your Render configuration:

Build Command:

pip install -r requirements.txt


Start Command:

gunicorn auth.wsgi:application --bind 0.0.0.0:$PORT


Add .env variables inside Render Dashboard → Environment

After disabling auto-deploy, deploy manually via:
Dashboard → Manual Deploy → Deploy Latest Commit


📦 Project Structure
django-chatapp/
│── auth/                  # Main Django project
│── chatapp/               # App with chat UI
│── static/                # CSS, JS, icons
│── templates/             # HTML templates
│── requirements.txt
│── Dockerfile
│── manage.py
└── README.md
