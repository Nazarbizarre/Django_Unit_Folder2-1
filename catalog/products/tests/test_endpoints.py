import pytest
from django.urls import reverse

from .fixtures import product, product_with_discount, order, category
from products.models import Product, Category, Cart, CartItem, Order, OrderItem

@pytest.mark.django_db
def test_products_list_empty(api_client):
    url = reverse('products:product-list')
    
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data == []

    
    
@pytest.mark.django_db
def test_products_list(api_client, product, product_with_discount):
    url = reverse('products:product-list')
    
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2

@pytest.mark.django_db
def test_product_detail(api_client, product):
    url = reverse('products:product-detail', args=[product.id])
    
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['name'] == product.name
    assert response.data['price'] == product.price
    assert response.data['discount'] == product.discount
    assert response.data['nomenclature'] == product.nomenclature
    assert response.data['category'] == product.category.id
