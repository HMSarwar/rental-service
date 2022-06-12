import json
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()
from products.models import Products


def import_data():
    with open('../backend-frontend-data.json', 'r') as f:
        data = json.loads(''.join(f.readlines()))
        for row in data:
            p = Products()
            for k, v in row.items():
                setattr(p, k, v)
            p.save()


if __name__ == '__main__':
    import_data()
