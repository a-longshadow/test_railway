# 🚀 Django Blog Application

[![Django](https://img.shields.io/badge/Django-4.2.7-green.svg)](https://djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)](https://postgresql.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1.3-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A full-featured, modern blogging platform built with Django and PostgreSQL. Features user authentication, CRUD operations, commenting system, and a beautiful responsive interface.

## ✨ Features

- 🔐 **Complete Authentication System** - User registration, login, logout
- 📝 **Blog Management** - Create, read, update, delete posts with rich editor
- 💬 **Interactive Comments** - User engagement and comment moderation
- 👑 **Admin Interface** - Superuser dashboard for content management
- 🎨 **Modern UI/UX** - Responsive design with Bootstrap 5 and custom CSS
- 🗄️ **PostgreSQL Database** - Robust, scalable database architecture
- 🛡️ **Security First** - CSRF protection, user permissions, environment variables
- 📱 **Mobile Responsive** - Perfect experience on all devices

## 🏠 Live Demo

Visit the live application: `http://127.0.0.1:8000/` (after local setup)

### Screenshots

**Homepage**
- Hero section with statistics
- Recent posts preview
- Modern design with gradients

**Blog Features**
- Post listing with pagination
- Detailed post view with comments
- Author-only edit/delete permissions

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL 15+
- pip and virtualenv

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/a-longshadow/test_railway.git
cd test_railway
```

2. **Set up virtual environment**
```bash
python3 -m venv blog_env
source blog_env/bin/activate  # On Windows: blog_env\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure PostgreSQL**
```bash
# Install PostgreSQL (macOS with Homebrew)
brew install postgresql@15
brew services start postgresql@15

# Create database
createdb blogdb
```

5. **Environment setup**
```bash
# Copy environment template
cp .env.example .env

# Edit .env with your database credentials
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=blogdb
DB_USER=your-username
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

6. **Database migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Create superuser**
```bash
python manage.py createsuperuser
```

8. **Start development server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see your blog!

## 🗂️ Project Structure

```
├── 📁 blogproject/         # Main Django project
│   ├── settings.py        # Configuration
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI config
├── 📁 blog/              # Blog application
│   ├── models.py         # Database models
│   ├── views.py          # View logic
│   ├── forms.py          # Form definitions
│   ├── urls.py           # Blog URLs
│   └── admin.py          # Admin interface
├── 📁 accounts/          # User authentication
│   ├── views.py          # Auth views
│   ├── forms.py          # User forms
│   └── urls.py           # Auth URLs
├── 📁 templates/         # HTML templates
│   ├── base.html         # Master template
│   ├── blog/            # Blog templates
│   └── accounts/        # Auth templates
├── 📁 static/           # Static assets
│   └── css/style.css    # Custom styles
├── 📁 docs/             # Documentation
│   └── best-practices/  # Best practices docs
├── 📋 requirements.txt   # Python dependencies
└── 🔧 manage.py         # Django management
```

## 🛣️ URL Routes

| Route | Description | Authentication |
|-------|-------------|----------------|
| `/` | Homepage with recent posts | Public |
| `/posts/` | All blog posts | Public |
| `/posts/create/` | Create new post | Required |
| `/posts/<id>/<slug>/` | Post detail with comments | Public |
| `/posts/<id>/edit/` | Edit post | Author only |
| `/posts/<id>/delete/` | Delete post | Author only |
| `/accounts/register/` | User registration | Public |
| `/accounts/login/` | User login | Public |
| `/accounts/logout/` | User logout | Authenticated |
| `/admin/` | Admin dashboard | Staff only |

## 🛠️ Built With

- **Backend:** Django 4.2.7, PostgreSQL 15
- **Frontend:** Bootstrap 5, Custom CSS, JavaScript
- **Forms:** Django Crispy Forms
- **Authentication:** Django's built-in auth system
- **Environment:** python-decouple for config management

## 📚 Documentation

Comprehensive documentation is available in the `docs/` folder:

- 📋 **[Project Documentation](docs/best-practices/project-documentation.md)** - Complete feature overview
- 🏗️ **[Architecture Overview](docs/best-practices/architecture-overview.md)** - Technical deep-dive
- ⚡ **[Quick Reference](docs/best-practices/quick-reference.md)** - Developer commands and patterns

## 🔒 Security Features

- ✅ CSRF protection on all forms
- ✅ User authentication and authorization
- ✅ Environment variable configuration
- ✅ SQL injection prevention via Django ORM
- ✅ XSS protection with template auto-escaping
- ✅ Secure password hashing

## 🚀 Deployment

### Railway Deployment

This project is configured for easy deployment on Railway:

1. Connect your GitHub repository to Railway
2. Set environment variables in Railway dashboard
3. Deploy automatically on push to main branch

### Environment Variables for Production

```bash
SECRET_KEY=your-production-secret-key
DEBUG=False
DB_NAME=your-production-db-name
DB_USER=your-production-db-user
DB_PASSWORD=your-production-db-password
DB_HOST=your-production-db-host
DB_PORT=5432
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django community for the excellent framework
- Bootstrap team for the responsive framework
- PostgreSQL developers for the robust database
- All contributors who help improve this project

## 📞 Support

If you encounter any issues or have questions:

- 📧 **Email:** [Create an issue](https://github.com/a-longshadow/test_railway/issues)
- 📖 **Documentation:** Check the `docs/` folder
- 🐛 **Bug Reports:** [GitHub Issues](https://github.com/a-longshadow/test_railway/issues)

---

**⭐ If you find this project helpful, please give it a star on GitHub!**

Built with ❤️ using Django, PostgreSQL, and modern web technologies. 