# Create your views here.
from .models import *
from .serializers import *
from rest_framework.permissions import (AllowAny)
from rest_framework.response import Response
from django.http import Http404
# import request
from django.conf import settings
from rest_framework import status, generics,mixins
# Create your views here.
class BuildersAPIView(generics.GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    queryset = Builders.objects.all().order_by('id')
    serializer_class = BuildersSerializer

    def get_object(self, id):
        try:

            return Builders.objects.get(id=id)
        except Builders.DoesNotExist:
            raise Http404

    def get(self, request,id=None, *args, **kwargs):
        if id:
            id_obj = self.get_object(id)
            serializer = BuildersSerializer(id_obj)
            return Response(serializer.data)
        else:
            alldata = Builders.objects.all()
            serializer = BuildersSerializer(alldata, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = BuildersSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,id=None, *args, **kwargs):
        agent_type = self.get_object(id)
        serializer = BuildersSerializer(agent_type, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # data = serializer.data
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, *args, **kwargs):
        try:
            Builders.objects.filter(id=id).delete()
            message = {"success": "sucessfully deleted"}
            return Response(message, status=status.HTTP_200_OK)
        except Exception as e:
            error = getattr(e, 'message', repr(e))
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

class SupplierAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = Supplier.objects.all().order_by('id')
    serializer_class = SupplierSerializer

    def get_object(self, id):
        try:
            return Supplier.objects.get(id=id)
        except Supplier.DoesNotExist:
            raise Http404

    def get(self, request, id=None, *args, **kwargs):
        if id:
            supplier_obj = self.get_object(id)
            serializer = SupplierSerializer(supplier_obj)
            return Response(serializer.data)
        else:
            alldata = Supplier.objects.all()
            serializer = SupplierSerializer(alldata, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = SupplierSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, *args, **kwargs):
        supplier_obj = self.get_object(id)
        serializer = SupplierSerializer(supplier_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, *args, **kwargs):
        try:
            Supplier.objects.filter(id=id).delete()
            message = {"success": "successfully deleted"}
            return Response(message, status=status.HTTP_200_OK)
        except Exception as e:
            error = getattr(e, 'message', repr(e))
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
