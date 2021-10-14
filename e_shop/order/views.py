# import stripe
from pypaystack import Transaction

from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem
from .serializers import OrderSerializer, MyOrderSerializer

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    # return Response(request.data, status=status.HTTP_201_CREATED)
    serializer = OrderSerializer(data=request.data)
    # return Response(serializer.initial_data, status=status.HTTP_201_CREATED)
    if serializer.is_valid():
        # return Response(serializer.validated_data['items'], status=status.HTTP_201_CREATED)
        paid_amount = serializer.validated_data['paid_amount']
        # total_cost = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])

        try:
            transaction = Transaction('sk_test_286c1cee07519622c029c24cfdee80af5380a952')
            response = transaction.verify(serializer.validated_data['reference_id'])

            if response[0] == 200:  # Check status code is success
                serializer.save(user=request.user, paid_amount=paid_amount, paid=True)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)