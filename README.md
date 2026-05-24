# 🛒 SnapCart | Django + React Ecommerce

SnapCart is a **full-featured ecommerce website** built with **Django** (backend) and **React + Redux** (frontend).  
It’s designed as a real-world project, developed in a linear and progressive manner, covering all essential ecommerce features.

---

## 🚀 Features
- **[Shopping cart](ca://s?q=Shopping_cart_in_Django_React)** with PayPal & credit/debit card payments
- **[Product rating & review](ca://s?q=Product_rating_and_review_in_Django_React)** system
- **[Admin area](ca://s?q=Admin_area_in_Django_React)** to manage customers, products & orders
- **[Product search](ca://s?q=Product_search_in_Django_React)** with carousel, pagination & filtering
- **[User authentication](ca://s?q=User_authentication_in_Django_React)** with registration, login, and profile management
- Responsive UI with **React**, **Redux**, and **Bootstrap**

---

## 🛠 Tech Stack
- **Frontend**: [React](ca://s?q=React_frontend), [Redux](ca://s?q=Redux_state_management), [JavaScript](ca://s?q=JavaScript_ES6), [Bootstrap](ca://s?q=Bootstrap_UI_framework)
- **Backend**: [Django](ca://s?q=Django_backend), [Django_REST_Framework](ca://s?q=Django_REST_Framework)
- **Database**: SQLite (default), easily switchable to PostgreSQL/MySQL
- **Payments**: [PayPal](ca://s?q=PayPal_integration_Django_React) & credit/debit card integration
- **Authentication**: JWT-based
- **API**: RESTful endpoints

---

## 📁 Project Structure

```bash
SnapCart/
├── backend/
│   ├── backend/          # Django core (settings, urls, wsgi, asgi)
│   ├── base/             # Ecommerce app
│   │   ├── migrations/   # Database migrations
│   │   ├── models.py     # Product, Order, User models
│   │   ├── serializers.py
│   │   ├── views/        # order_views, product_views, user_views
│   │   ├── urls/         # order_urls, product_urls, user_urls
│   │   └── admin.py, tests.py, signals.py
│   ├── frontend/         # React frontend
│   │   ├── public/       # Static assets (images, logos, manifest)
│   │   ├── src/
│   │   │   ├── actions/      # Redux actions
│   │   │   ├── components/   # Header, Footer, Product, Rating, Loader, etc.
│   │   │   ├── constants/    # Redux constants
│   │   │   ├── reducers/     # Redux reducers
│   │   │   ├── pages/        # Cart, Checkout, Home, Login, Order, Payment, Profile, Register, Shipping
│   │   │   ├── store.js      # Redux store
│   │   │   └── App.js, index.js, index.css
│   │   └── package.json, README.md
│   ├── static/           # CSS, JS, images
│   ├── db.sqlite3
│   ├── manage.py
│   └── requirements.txt
├── resources/            # Logos, favicons
└── README.md
```


## ⚙️ Installation

### Backend (Django)
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

### Frontend (React)
```bash
cd backend/frontend

# Install dependencies
npm install

# Start development server
npm start
```
