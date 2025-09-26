# CyberAcademyChallengeAPI

A REST API for managing cybersecurity training resources. Built with **Django** and **Django REST Framework**, the API supports full CRUD operations and uses **JWT authentication with cookies**.

---

## 📑 Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Authentication](#authentication)
- [API Endpoints](#api-endpoints)
- [DRF Web Interface Guide](#drf-web-interface-guide)

---

## ⚙️ Installation

To set up the project, follow these steps:

1.  **Clone the repository**
    ```bash
    git clone <your-repo-url>
    cd CyberAcademyChallengeAPI
    ```

2.  **Create a virtual environment**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment**
    * **Windows (Command Prompt):**
        ```bash
        venv\Scripts\activate.bat
        ```
    * **Windows (PowerShell):**
        ```bash
        venv\Scripts\Activate.ps1
        ```
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🔧 Setup

After installing the dependencies, you need to set up the database and run the development server.

1.  **Run migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

2.  **Run the development server**
    ```bash
    python manage.py runserver
    ```
    The API will now be accessible at `http://127.0.0.1:8000`.

---

## 🔐 Authentication

This API uses **JWT authentication with cookies**. All endpoints require authentication and are accessible via the Django REST Framework web interface.

* **Default Admin Credentials**
    * **Username:** `admin`
    * **Password:** `admin`

* **Registration**
    * **URL:** `/api/auth/registration/`
    * **Description:** Use this endpoint to register a new user if needed.

---

## 🔌 API Endpoints

### 🔍 List All Resources

* **URL:** `/api/resources/`
* **Method:** `GET`
* **Description:** Retrieve all resources.
* **Features:** Supports filtering, search, and ordering.
    * **DRF Web Interface Features:**
        * Filter by category
        * Search in title and description
        * Order by ID or title

### ➕ Create Resource

* **URL:** `/api/resources/create/`
* **Method:** `POST`
* **Description:** Add a new resource.
* **Fields:**
    * `title` (max 20 characters)
    * `description` (max 5000 characters, optional)
    * `category` (select from predefined choices)
    * `link` (full URL, optional, must be unique)

### ✏️ Update Resource

* **URL:** `/api/resources/<id>/update/`
* **Method:** `PUT` or `PATCH`
* **Description:** Update an existing resource (full or partial update).
* **Fields:** Same as for the `Create Resource` endpoint.

### 🗑️ Delete Resource

* **URL:** `/api/resources/<id>/delete/`
* **Method:** `DELETE`
* **Description:** Delete a resource by its ID.

---

## 🌐 DRF Web Interface Guide

The Django REST Framework provides a web interface that's useful for testing endpoints directly in the browser.

### 🔑 Logging In to Get the JWT Cookie

* **Log In URL:** `/api/auth/login/`
* **Action:** You must log in here to obtain the necessary **JWT cookie** required to access all protected resource endpoints.
![DRF Login UI](/images/login.png)

---

### 🔍 Viewing All Resources

* **URL:** `/api/resources/`
* **Action:** View the list of all resources, and use the filters/search bars provided by DRF.
![DRF Resources List UI](/images/resources.png)

---

### ➕ Creating a Resource

* **URL:** `/api/resources/create/`
* **Action:** Use the form provided to submit a new resource object.
![DRF Create Resource UI](/images/create_resource.png)

---

### ✏️ Updating a Resource

* **URL:** `/api/resources/<id>/update/`
* **Action:** Navigate to this URL, replacing `<id>` with the target resource's ID, to update its details.
![DRF Update Resource UI](/images/update_resource.png)

---

### 🗑️ Deleting a Resource

* **URL:** `/api/resources/<id>/delete/`
* **Action:** Navigate to this URL, replacing `<id>` with the target resource's ID, and confirm deletion.
![DRF Delete Resource UI](/images/delete_resource.png)

---