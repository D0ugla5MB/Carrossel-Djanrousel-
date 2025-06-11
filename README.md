# Web Carousel Application

## 1. Project Overview

A web app for registered users to create, organize, and share image carousels. Images require text descriptions. Users manage their carousels and image details.

---

## 2. Key Features

* **User Accounts**: Secure sign-up, login, logout. Users manage their own content.
* **Carousels**: Create, view, edit, delete carousels (title, public/private).
* **Image Management**: Upload (drag-and-drop), mandatory editable descriptions, delete images. Display order is upload order (optional reordering).
* **Roles & Permissions**:
  * **User**: Manages own carousels/images, profile. Views public carousels.
  * **Admin**: Manages all content and user accounts.
  * **Super Admin**: System-wide settings, role management.
* **User Profiles**: Edit display name, avatar, bio. Manage account settings (password, deactivation).

---

## 3. Technical Architecture

### Core Technologies

* **Backend**: Django 5.2.1 (Python 3.11)
* **Frontend**: Vanilla JS (HTML, CSS)
* **Database**: Postgress 17; Google Cloud SQL (Prod), SQLite (Dev)
* **Image Storage**: Google Cloud Storage
* **Deployment**: Google Cloud Run

### Data Model

* **Entities**: `Users`, `Carousels`, `Images`.
* **Relationships**: Users have Carousels; Carousels have Images.

### Cloud Integration

* **Google Cloud Run**: Hosts the Django application.
* **Google Cloud Storage (GCS)**: Stores all images.
* **Google Cloud SQL**: Managed database for production.

### Frontend & UI/UX

* Responsive design for desktop, tablet, mobile.
* Accessibility (WCAG) considerations.
* Vanilla JS for interactivity.

---

## 4. Deployment

* **Platform**: Google Cloud Run (Prod).
* **Environments**: Separate development (local/cloud) and production (Google Cloud) setups.
* **Configuration**: Use environment variables for sensitive data

---

## 5. Security Highlights

* Input validation (client & server-side).
* CSRF protection (Django built-in).
* Secure password hashing (Django's default PBKDF2).
* HTTPS enforced in production.
* Regular dependency updates.
