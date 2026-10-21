from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        
        base_url = "/products"
        detail_url = f"/products/{instance.id}/"
        
        response['_links'] = [
            {"rel": "self", "href": base_url, "action": "POST", "types": ["application/json"]},
            {"rel": "self", "href": detail_url, "action": "GET", "types": ["application/json"]},
            {"rel": "self", "href": detail_url, "action": "PUT", "types": ["application/json"]},
            {"rel": "self", "href": detail_url, "action": "DELETE", "types": ["application/json"]}
        ]
        
        return response