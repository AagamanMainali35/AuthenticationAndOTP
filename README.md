  Authenticator – Django & SQLite OTP Authentication  

Authenticator – Django & SQLite OTP Authentication
==================================================

This is an **Authentication System** built using **Django**, **HTML**, and **SQLite**, featuring **OTP-based verification** via email. Users can securely register, log in, and verify their identity using a One-Time Password (OTP) sent via email.

🚀 Features
-----------

*   🔐 **User Authentication** – Secure login and registration system.
*   📩 **OTP Verification** – Sends OTP via email for verification.
*   🔄 **Password Reset with OTP** – Users can reset passwords using email-based OTP authentication.
*   💾 **SQLite Database** – Uses SQLite for lightweight and easy database management.
*   🎨 **Frontend**: Simple and clean HTML/CSS UI.
*   📨 **Django Send Mail** – Sends OTP emails using Django's built-in email service.

🛠 Tech Stack
-------------

*   **Backend:** Django (Python)
*   **Frontend:** HTML, CSS
*   **Database:** SQLite
*   **Email Service:** Django Send Mail

📦 Installation
---------------

Follow these steps to get your Django OTP-based authentication system up and running:

### 1\. Clone the repository:

    git clone https://github.com/yourusername/your-repository-name.git
    cd your-repository-name

### 2\. Create a virtual environment (optional but recommended):

    python -m venv venv

### 3\. Activate the virtual environment:

\- **Windows:**

    venv\Scripts\activate

\- **Mac/Linux:**

    source venv/bin/activate

### 4\. Install the required dependencies:

    pip install -r requirements.txt

### 5\. Set up your .env file for environment variables:

    cp .env.example .env

Edit the .env file with your specific values:

    SECRET_KEY=django-insecure-cb1vos3+te$zj_p56*r%8_ryymioi(a2xp!vf2^)2c3il3jykf
    DATABASE_ENGINE=django.db.backends.sqlite3
    DATABASE_NAME=path_to_your_project/db.sqlite3
    ALLOWED_HOSTS=localhost,127.0.0.1
    EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=587
    EMAIL_USE_TLS=True
    EMAIL_HOST_USER=jewsfryer69@gmail.com
    EMAIL_HOST_PASSWORD=qfhb eqvo imee bocu

### 6\. Run the migrations to set up the database:

    python manage.py migrate

### 7\. Create a superuser to access the Django admin panel (optional):

    python manage.py createsuperuser

### 8\. Run the development server:

    python manage.py runserver

You can now access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

🔐 Configuration
----------------

Create a .env file in the root directory and add the following:

    SECRET_KEY=django-insecure-cb1vos3+te$zj_p56*r%8_ryymioi(a2xp!vf2^)2c3il3jykf
    DATABASE_ENGINE=django.db.backends.sqlite3
    DATABASE_NAME=path_to_your_project/db.sqlite3
    ALLOWED_HOSTS=localhost,127.0.0.1
    EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=587
    EMAIL_USE_TLS=True
    EMAIL_HOST_USER=jewsfryer69@gmail.com
    EMAIL_HOST_PASSWORD=qfhb eqvo imee bocu

*   **SECRET\_KEY**: A random secret key for Django.
*   **DATABASE\_NAME**: Path to your SQLite database (e.g., db.sqlite3).
*   **DATABASE\_ENGINE**: Use django.db.backends.sqlite3 for SQLite.
*   **Email Settings:**
    *   **EMAIL\_BACKEND**: Set this to django.core.mail.backends.smtp.EmailBackend.
    *   **EMAIL\_HOST**: SMTP server for sending emails (e.g., smtp.gmail.com).
    *   **EMAIL\_PORT**: Port for sending emails (e.g., 587).
    *   **EMAIL\_USE\_TLS**: Set to True to use TLS.
    *   **EMAIL\_HOST\_USER**: Your email address.
    *   **EMAIL\_HOST\_PASSWORD**: Your email password.

📝 License
----------

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.