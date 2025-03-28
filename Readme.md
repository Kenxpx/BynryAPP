# Gas Utility Customer Service Portal

A full-featured **Django + React** web application designed for a gas utility company to manage customer service requests efficiently. This platform allows users to submit, track, and manage service requests while providing customer support representatives with tools for effective resolution.

## **Repository**
GitHub: [BynryAPP](https://github.com/Kenxpx/BynryAPP.git)

---

## **Key Features**

### **Infrastructure**
- Production-ready **NGINX** configuration
- **PostgreSQL** setup with security best practices

### **Frontend & UI**
- **Responsive design** (mobile-first approach)
- **Real-time status updates**
- **Dashboard analytics cards**
- **File attachment management**

### **User Experience Enhancements**
- **Status indicators** & priority coloring
- **Interactive guided tour system**

### **Templates & Permissions**
- **Consistent UI** across all pages
- **Permission-based** content display

### **Testing**
- **Comprehensive model tests**
- **View authentication tests**
- **Fixtures for test data**
- **User type validation**

---

## **Setup & Installation**

### **1. Clone the Repository**
```sh
git clone https://github.com/Kenxpx/BynryAPP.git
cd BynryAPP
```

### **2. Create Required Template Includes**
Inside `templates/includes/`, create the following files:
- `navbar.html`
- `messages.html`
- `footer.html`

Then, run:
```sh
python manage.py collectstatic
```

---

## **Docker Deployment**

### **1. Build & Start Containers**
```sh
docker-compose up --build -d
```

### **2. Run Migrations & Collect Static Files**
```sh
docker exec -it gas_utility_backend python manage.py migrate
docker exec -it gas_utility_backend python manage.py collectstatic --noinput
```

### **3. Create a Superuser**
```sh
docker exec -it gas_utility_backend python manage.py createsuperuser
```

### **4. Access the Application**
- **Frontend (React/Vue):** `http://localhost:3000`
- **Backend (Django API):** `http://localhost:8000`
- **Admin Panel:** `http://localhost:8000/admin/`

---

## **Local Development Setup (Without Docker)**

### **1. Install Dependencies**
```sh
pip install -r backend/requirements.txt
cd frontend && npm install
```

### **2. Run Backend**
```sh
python manage.py runserver
```

### **3. Run Frontend**
```sh
cd frontend
npm start
```

---

## **Testing**
Run Django tests:
```sh
docker exec -it gas_utility_backend pytest
```

---

For additional details, refer to the [GitHub repository](https://github.com/Kenxpx/BynryAPP.git). 🚀

