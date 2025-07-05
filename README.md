
# Django-CRM

Django-CRM is an open-source, fully functional Customer Relationship Management (CRM) web application built with Django. It helps manage customers, leads, contacts, and sales pipelines efficiently. This project is a great example for learning Django and building scalable web applications.

---

## 🚀 Features

- Lead management system  
- Customer management  
- User authentication & authorization (sign-up, login, logout)  
- Responsive UI with Bootstrap  
- Role-based access controls  
- Dashboard with data insights  
- Activity logs and comments  
- Easy to extend and customize  

---

## 🔧 Tech Stack

- **Backend:** Django, Python  
- **Frontend:** HTML, CSS (Bootstrap), JavaScript  
- **Database:** MySQL, easy to switch to PostgreSQL or other
- **Other:** Django Templates, 

---

## ⚙️ Installation

### Prerequisites
- Python 3.x
- pip
- virtualenv (optional but recommended)

### Setup

```bash
# Clone the repository
git clone https://github.com/flatplanet/Django-CRM.git
cd Django-CRM

# Create a virtual environment
python -m venv env
 env\Scripts\activate  # On Windows use: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---



## 🔑 Admin Access

After creating a superuser, access the Django admin panel at: 

`http://127.0.0.1:8000/admin/`


---

## 🔑 Images 
LOGIN page:
 ![Login](https://github.com/user-attachments/assets/1df0f2a5-4553-49d3-b0b7-ab4a19980355)
Home page:
 ![Home-Record](https://github.com/user-attachments/assets/4cc6bada-d647-4aa4-a7cc-2bd76f3b9da1)
Add Record:
 ![Add Record](https://github.com/user-attachments/assets/1a2b6e0c-a20a-4576-8802-c6baf4a51103)
Update record:
 ![Update](https://github.com/user-attachments/assets/491bcd4e-687e-4c63-9573-04778dcb867d)

