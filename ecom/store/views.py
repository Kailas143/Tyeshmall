from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import location, store
from .serializers import location_serializers, store_serializers


class store_data(generics.GenericAPIView,APIView) :
    serializer_class=store_serializers

    def post(self,request) :
        data={}
        serializer=store_serializers(data=request.data)
        if serializer.is_valid():
            store=serializer.save()
            data['success']="successfully added"
        else :
            data['error']= "Data not valid"
        return Response(data)

class location_data(generics.GenericAPIView,APIView) :
    
    serializer_class=location_serializers
    

    def post(self,request) :
        data={}
        serializer=location_serializers(data=request.data)
        if serializer.is_valid():
            location=serializer.save()
            data['success']="successfully added"
        else :
            data['error']= "Data not valid"
        return Response(data)

class location_generics(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin) :
    serializer_class=location_serializers
    queryset=location.objects.all()

    def get(self,request) :
        return self.list(request)

    def post(self,request) :
        return self.create(request)

class store_generics(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin) :
    serializer_class=store_serializers
    queryset=store.objects.all()

    def get(self,request) :
        return self.list(request)

    def post(self,request) :
        return self.create(request)



class store_update(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    serializer_class=store_serializers
    queryset=store.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        return self.list(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.delete(request, id)

class location_update(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    serializer_class=location_serializers
    queryset=location.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        return self.list(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.delete(request, id)


class store_product(generics.GenericAPIView,APIView):
    serializer_class=store_serializers
    queryset=store.objects.all()

    def filter_product(self,pid):
        stp=store.objects.filter(product=pid)
        return stp
    
    def get(self,request,pid):
        str_p=self.filter_product(pid)
        store=store_serializers(str_p,many=True)
        return Response(store.data)

class location_store(generics.GenericAPIView,APIView):
    serializer_class=location_serializers
    queryset=location.objects.all()

    def filter_product(self,sid):
        stp=location.objects.filter(store_id=sid)
        return stp
    
    def get(self,request,sid):
        str_p=self.filter_product(sid)
        store=store_serializers(str_p,many=True)
        return Response(store.data)