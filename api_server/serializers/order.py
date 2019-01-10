from rest_framework import serializers
from api_server import models
from djmoney.models.fields import MoneyField

class OrderListSerializer(serializers.ModelSerializer):

    number = serializers.CharField(source='get_number', read_only=True)

    subtotal = MoneyField()
    total = MoneyField()

    class Meta:
        model = models.Order
        fields = '__all__'

    
    read_only_fields = ['shipping_address_text']

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OrderItem
        fields = '__all__'

class OrderDetailSerializer(OrderListSerializer):
    items = OrderItemSerializer(
        many=True,
        read_only=True,
    )

    amount_paid = MoneyField()
    outstanding_amount = MoneyField()
    cancelable = serializers.BooleanField(read_only=True)

    is_partially_paid = serializers.SerializerMethodField(
        method_name='get_partially_paid',
        help_text="Returns true, if order has been partially paid",
    )

    annotation = serializers.CharField(
        write_only=True,
        required=False,
    )

    reorder = serializers.BooleanField(
        write_only=True,
        default=False,
    )

    cancel = serializers.BooleanField(
        write_only=True,
        default=False,
    )

    class Meta:
        model = models.Order
        exclude = ['id', 'customer','_subtotal', '_total']
        read_only_fields = ['shipping_address_text']

    def get_paid(self, order):
        return order.amount_paid > 0
