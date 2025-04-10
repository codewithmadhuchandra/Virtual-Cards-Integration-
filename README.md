# Virtual Cards Integration System

A Django application that enables users to create virtual cards for invoices and track transactions made using these cards.

## Features

- Create and manage invoices
- Generate virtual cards for invoices
- Process payments using virtual cards
- Track transaction history
- User-friendly interface

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/codewithmadhuchandra/Virtual-Cards-Integration-.git
cd .\Virtual-Cards-Integration-\
```

2. Create and activate a virtual environment:
```bash
python -m venv venv

.\venv\Scripts\activate

```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (optional, for admin access):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the application at `http://127.0.0.1:8000/`

## Usage

1. **Invoices**
   - Navigate to `/invoices/` to view all invoices
   - Click "Create New Invoice" to create an invoice
   - Each invoice can have one virtual card

2. **Virtual Cards**
   - Navigate to `/virtual-cards/` to view all virtual cards
   - Create a virtual card for an invoice from the invoice list
   - Each card has a unique number, expiry date, and CVV

3. **Transactions**
   - Navigate to `/transactions/` to view all transactions
   - Make payments using virtual cards
   - Track payment status and history

## Project Structure

- `vc_app/` - Main application directory
  - `models.py` - Database models
  - `views.py` - View functions and classes
  - `forms.py` - Form definitions
  - `urls.py` - URL routing
  - `templates/` - HTML templates
- `vc_project/` - Project configuration
  - `settings.py` - Django settings
  - `urls.py` - Main URL configuration

