import pytest
from django.urls import reverse
import uuid

from .fixtures import product, product_with_discount, order, category
from products.models import Product, Category, Cart, CartItem, Order, OrderItem
from ..models import User



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



@pytest.mark.django_db
def test_product_detail_not_found(api_client):
    url = reverse('products:product-detail',kwargs={'pk':124312})

    response = api_client.get(url)

    assert response.status_code == 404


@pytest.mark.django_db
def test_update_product(api_client, product, super_user):

    url = reverse('products:product-detail',kwargs={'pk':product.id})
    api_client.force_authenticate(super_user)

    response = api_client.patch(url, data={'price':1573})

    assert response.status_code == 200
    assert response.data.get('price') == 1573
    assert product.price == 100


@pytest.mark.django_db
def test_create_product(api_client, category, super_user):

    url = reverse("products:product-list")
    data = {
        "name":"test_name",
        "description":"test_description",
        "category":category.id,
        "nomenclature":str(uuid.uuid4()),
    }
    api_client.force_authenticate(super_user)

    response = api_client.post(url, data=data)

    assert response.status_code == 201
    assert response.data.get('name') == "test_name"
    assert Product.objects.filter(id=response.data.get("id")).exists()