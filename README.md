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

## 📂 Project Structure
├── backend
│   ├── backend
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── base
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_order_orderitem_review_shippingaddress.py
│   │   │   ├── 0003_product_image.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── products.py
│   │   ├── serializers.py
│   │   ├── signals.py
│   │   ├── tests.py
│   │   ├── urls
│   │   │   ├── order_urls.py
│   │   │   ├── product_urls.py
│   │   │   └── user_urls.py
│   │   └── views
│   │       ├── order_views.py
│   │       ├── product_views.py
│   │       └── user_views.py
│   ├── db.sqlite3
│   ├── frontend
│   │   ├── build
│   │   │   ├── asset-manifest.json
│   │   │   ├── favicon.ico
│   │   │   ├── images
│   │   │   │   ├── airpods.jpg
│   │   │   │   ├── alexa.jpg
│   │   │   │   ├── camera.jpg
│   │   │   │   ├── mouse.jpg
│   │   │   │   ├── phone.jpg
│   │   │   │   ├── playstation.jpg
│   │   │   │   └── sample.jpg
│   │   │   ├── index.html
│   │   │   ├── logo192.png
│   │   │   ├── logo512.png
│   │   │   ├── manifest.json
│   │   │   ├── robots.txt
│   │   │   └── static
│   │   │       ├── css
│   │   │       │   ├── main.4bb19502.chunk.css
│   │   │       │   └── main.4bb19502.chunk.css.map
│   │   │       └── js
│   │   │           ├── 2.23e93b8b.chunk.js
│   │   │           ├── 2.23e93b8b.chunk.js.LICENSE.txt
│   │   │           ├── 2.23e93b8b.chunk.js.map
│   │   │           ├── 3.024b28d9.chunk.js
│   │   │           ├── 3.024b28d9.chunk.js.map
│   │   │           ├── main.a989b901.chunk.js
│   │   │           ├── main.a989b901.chunk.js.map
│   │   │           ├── runtime-main.18617dd7.js
│   │   │           └── runtime-main.18617dd7.js.map
│   │   ├── package.json
│   │   ├── package-lock.json
│   │   ├── public
│   │   │   ├── favicon.ico
│   │   │   ├── images
│   │   │   │   ├── airpods.jpg
│   │   │   │   ├── alexa.jpg
│   │   │   │   ├── camera.jpg
│   │   │   │   ├── mouse.jpg
│   │   │   │   ├── phone.jpg
│   │   │   │   ├── playstation.jpg
│   │   │   │   └── sample.jpg
│   │   │   ├── index.html
│   │   │   ├── logo192.png
│   │   │   ├── logo512.png
│   │   │   ├── manifest.json
│   │   │   └── robots.txt
│   │   ├── README.md
│   │   ├── src
│   │   │   ├── actions
│   │   │   │   ├── cartActions.js
│   │   │   │   ├── orderActions.js
│   │   │   │   ├── productActions.js
│   │   │   │   └── userActions.js
│   │   │   ├── App.js
│   │   │   ├── bootstrap.min.css
│   │   │   ├── components
│   │   │   │   ├── Footer.js
│   │   │   │   ├── FormContainer.js
│   │   │   │   ├── Header.js
│   │   │   │   ├── Loader.js
│   │   │   │   ├── Message.js
│   │   │   │   ├── Product.js
│   │   │   │   └── Rating.js
│   │   │   ├── constants
│   │   │   │   ├── cartConstants.js
│   │   │   │   ├── orderConstants.js
│   │   │   │   ├── productConstants.js
│   │   │   │   └── userConstants.js
│   │   │   ├── index.css
│   │   │   ├── index.js
│   │   │   ├── logo.svg
│   │   │   ├── pages
│   │   │   │   ├── CartPages.js
│   │   │   │   ├── CheckoutSteps.js
│   │   │   │   ├── HomePages.js
│   │   │   │   ├── LoginPages.js
│   │   │   │   ├── OrderPages.js
│   │   │   │   ├── PaymentPages.js
│   │   │   │   ├── PlaceOrderPages.js
│   │   │   │   ├── ProductPages.js
│   │   │   │   ├── ProfilePages.js
│   │   │   │   ├── RegisterPages.js
│   │   │   │   └── ShippingPages.js
│   │   │   ├── products.js
│   │   │   ├── reducers
│   │   │   │   ├── cartReducers.js
│   │   │   │   ├── orderReducers.js
│   │   │   │   ├── productReducers.js
│   │   │   │   └── userReducers.js
│   │   │   ├── reportWebVitals.js
│   │   │   └── store.js
│   │   └── yarn.lock
│   ├── manage.py
│   ├── requirements.txt
│   └── static
│       ├── css
│       ├── images
│       │   ├── airpods_fASkfKU.jpg
│       │   ├── airpods.jpg
│       │   ├── airpods_oYVARAQ.jpg
│       │   ├── alexa.jpg
│       │   ├── camera.jpg
│       │   ├── mouse.jpg
│       │   ├── phone.jpg
│       │   └── playstation.jpg
│       └── js


---

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