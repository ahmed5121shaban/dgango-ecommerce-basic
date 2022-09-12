import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')


import django
django.setup()

from faker import Faker
import random
from products.models import Product,Brand,Category

def seed_brand(n):
    fake = Faker()
    image = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg']

    for _ in range(n):
        name = fake.name()
        image = f'brand/{image[random.randint(0,5)]}'
        Brand.objects.create(
            name=name,
            image=image,
        )


def seed_category(n):
    fake = Faker()
    image = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg']

    for _ in range(n):
        name = fake.name()
        image = f'category/{image[random.randint(0,4)]}'
        Category.objects.create(
            name = name,
            image =image,
        )

def seed_product(n):
    
    fake = Faker()
    image = ['1.jpg','2.jpg','3.jpg','4.jpg','6.jpg','7.jpg','8.jpg',
    '9.jpg','10.jpg','11.jpg','12.jpg']
    flag_type = ['New','Feature','Sale']
    for _ in range(n):
        name = fake.name()
        sku = random.randint(1,100000)
        suptitle = fake.text(max_nb_chars = 300)
        desc = fake.text(max_nb_chars = 10000)
        flag = flag_type[random.randint(0,2)]
        price = round(random.uniform(20.99,99.99),2)
        image = f'prodect-image/{image[random.randint(0,11)]}'
        category = Category.objects.get(id=random.randint(1,5))
        brand = Brand.objects.get(id=random.randint(1,6))
        Product.objects.create(
            name = name,
            image =image,
            sku = sku,
            suptitle = suptitle,
            desc = desc,
            flag = flag,
            price = price,
            category = category,
            brand = brand,
            vedio = 'https://youtu.be/o0XbHvKxw7Y'
        )



#seed_brand(10)
#seed_category(10)
seed_product(100)