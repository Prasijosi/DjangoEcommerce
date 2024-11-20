from django.shortcuts import render
from django.db.models import query
from .models import Product
from .serializers import ProductSerializer,MessageSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from .tests import Message
# Create your views here.

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def listproducts(request):
    query = Product.objects.all()#get model data and seialize it
    serializer_class = ProductSerializer(query, many=True)#
    context = {
        'serializer_class_data':serializer_class.data
    }
    return Response(serializer_class.data) 

def listmessages(request):
    message_object = Message("Sending Message","Hi")
    serializer_class = MessageSerializer(many=True)
    return Response(serializer_class.data)
    