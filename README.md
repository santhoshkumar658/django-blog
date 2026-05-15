# Blog Project

A Django-based blog application with a public blog frontend and an admin-style dashboard for managing posts, categories, and users.

## Features

- User registration, login, and logout
- Homepage with featured and published blog posts
- Blog posts grouped by category
- Slug-based blog detail pages
- Comment system for blog posts
- Search posts by title, description, or content
- Dashboard for managing:
  - Categories
  - Blog posts
  - Users
- About section and social links support
- Image upload support for featured blog images

## Tech Stack

- Python
- Django
- SQLite
- Django Crispy Forms
- Crispy Bootstrap 4
- Pillow

## Project Structure

```bash
blog project/
├── assignments/      # About and social links models
├── blogs/            # Blog models, views, URLs, context processors
├── dashboards/       # Dashboard views, forms, and management pages
├── blog_main/        # Project settings, root URLs, forms, static files
├── templates/        # Frontend and dashboard templates
├── media/            # Uploaded images
├── manage.py
├── requirements.txt
└── db.sqlite3
