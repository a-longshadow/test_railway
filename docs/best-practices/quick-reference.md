# Django Blog - Quick Reference Guide

## 🚀 Quick Start Commands

### **Development Setup**
```bash
# Activate virtual environment
source blog_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

### **Database Operations**
```bash
# Create new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database (BE CAREFUL!)
python manage.py flush

# Create database backup
pg_dump blogdb > backup.sql

# Restore database
psql blogdb < backup.sql
```

### **Django Management**
```bash
# Open Django shell
python manage.py shell

# Collect static files (for production)
python manage.py collectstatic

# Run Django tests
python manage.py test

# Create new Django app
python manage.py startapp appname
```

## 🗂️ Project Structure Quick Map

```
📦 Key Files & Folders
├── 🔧 manage.py              # Django management script
├── 📋 requirements.txt       # Python dependencies
├── 🌐 .env                   # Environment variables
├── ⚙️ blogproject/settings.py # Main configuration
├── 🛣️ blogproject/urls.py     # Main URL routing
├── 📊 blog/models.py         # Database models
├── 👁️ blog/views.py          # View logic
├── 📋 blog/forms.py          # Form definitions
├── 🎨 templates/             # HTML templates
└── 📁 static/css/style.css   # Custom styles
```

## 🗄️ Model Quick Reference

### **Post Model**
```python
Post.objects.all()                    # Get all posts
Post.objects.filter(published=True)   # Published posts only
Post.objects.filter(author=user)      # Posts by specific user
Post.objects.create(title="...", content="...", author=user)
```

### **Comment Model**
```python
Comment.objects.filter(post=post)     # Comments for specific post
Comment.objects.filter(active=True)   # Active comments only
Comment.objects.create(post=post, author=user, content="...")
```

### **User Model**
```python
User.objects.all()                    # All users
User.objects.filter(is_staff=True)    # Staff users
User.objects.create_user(username="...", email="...", password="...")
```

## 🛣️ URL Patterns Reference

### **Blog URLs**
| URL Pattern | View | Template | Purpose |
|-------------|------|----------|---------|
| `/` | `home_view` | `blog/home.html` | Homepage |
| `/posts/` | `PostListView` | `blog/post_list.html` | All posts |
| `/posts/create/` | `PostCreateView` | `blog/post_form.html` | Create post |
| `/posts/<int:pk>/<slug:slug>/` | `PostDetailView` | `blog/post_detail.html` | Post detail |
| `/posts/<int:pk>/edit/` | `PostUpdateView` | `blog/post_form.html` | Edit post |
| `/posts/<int:pk>/delete/` | `PostDeleteView` | `blog/post_confirm_delete.html` | Delete post |

### **Account URLs**
| URL Pattern | View | Template | Purpose |
|-------------|------|----------|---------|
| `/accounts/register/` | `UserRegistrationView` | `accounts/register.html` | Register |
| `/accounts/login/` | `CustomLoginView` | `accounts/login.html` | Login |
| `/accounts/logout/` | `CustomLogoutView` | - | Logout |

## 🎨 Template Tags & Filters

### **Commonly Used Template Tags**
```django
{% extends 'base.html' %}             # Template inheritance
{% load static %}                     # Load static files
{% load crispy_forms_tags %}          # Load crispy forms
{% url 'blog:home' %}                 # URL reversal
{% csrf_token %}                      # CSRF protection
```

### **Useful Filters**
```django
{{ post.content|truncatewords:20 }}   # Truncate to 20 words
{{ post.created_at|date:"M d, Y" }}   # Format date
{{ post.content|linebreaks }}         # Convert newlines to <br>
{{ user.get_full_name|default:user.username }}  # Default value
```

## 🔐 Permission Checks

### **View-Level Permissions**
```python
# Require login
@login_required
def my_view(request):
    pass

# Class-based view login
class MyView(LoginRequiredMixin, View):
    pass

# Custom permission check
class PostUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user == self.get_object().author
```

### **Template-Level Checks**
```django
{% if user.is_authenticated %}
    <!-- Content for logged in users -->
{% else %}
    <!-- Content for anonymous users -->
{% endif %}

{% if user == post.author %}
    <!-- Content for post author only -->
{% endif %}

{% if user.is_staff %}
    <!-- Content for staff users -->
{% endif %}
```

## 📋 Form Handling Patterns

### **Basic Form Processing**
```python
def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process form data
            form.save()
            messages.success(request, 'Success!')
            return redirect('success_url')
    else:
        form = MyForm()
    return render(request, 'template.html', {'form': form})
```

### **Model Form with Custom Logic**
```python
def form_valid(self, form):
    form.instance.author = self.request.user
    form.instance.slug = slugify(form.instance.title)
    messages.success(self.request, 'Post created!')
    return super().form_valid(form)
```

## 🎨 CSS Classes Reference

### **Bootstrap Classes Used**
```css
/* Layout */
.container, .container-fluid
.row, .col-*, .col-md-*, .col-lg-*

/* Components */
.btn, .btn-primary, .btn-outline-primary
.card, .card-body, .card-title
.navbar, .nav-link, .dropdown

/* Utilities */
.mt-*, .mb-*, .mx-*, .py-*
.text-center, .text-muted
.d-flex, .justify-content-*
```

### **Custom CSS Classes**
```css
/* Custom components */
.card-post              /* Blog post cards */
.hero-section           /* Homepage hero */
.post-meta              /* Post metadata */
.comment-section        /* Comments area */
.form-container         /* Form styling */
.btn-custom             /* Custom buttons */
```

## 🐛 Common Issues & Solutions

### **Database Issues**
```bash
# Migration conflicts
python manage.py migrate --fake-initial

# Reset migrations (BE CAREFUL!)
rm blog/migrations/0001_initial.py
python manage.py makemigrations blog
python manage.py migrate

# Check migration status
python manage.py showmigrations
```

### **Static Files Not Loading**
```bash
# Ensure STATIC_URL and STATICFILES_DIRS are set
# Check settings.py:
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Collect static files for production
python manage.py collectstatic
```

### **Environment Variables**
```bash
# Create .env file with:
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=blogdb
DB_USER=your-username
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

## 📊 Useful Django Shell Commands

```python
# Enter Django shell
python manage.py shell

# Common operations
from blog.models import Post, Comment
from django.contrib.auth.models import User

# Create test data
user = User.objects.create_user('testuser', 'test@example.com', 'password')
post = Post.objects.create(title='Test Post', content='Test content', author=user)

# Query data
posts = Post.objects.filter(published=True)
comments = Comment.objects.filter(post=post, active=True)

# Bulk operations
Post.objects.filter(author=user).update(published=True)
Comment.objects.filter(post=post).delete()
```

## 🔍 Debugging Tips

### **Django Debug Toolbar** (Future Enhancement)
```python
# Add to settings.py for development
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INTERNAL_IPS = ['127.0.0.1']
```

### **Logging Configuration**
```python
# Add to settings.py for better debugging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
```

---

**Keep this guide handy for quick reference during development! 🚀** 