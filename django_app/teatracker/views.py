from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item, Entry, Location
from .serializers import ItemSerializer

# def tea_entry(request):
#     locations = None
#     items = None# load all items
#     return render(request, 'blog/blog_home.html', {"posts": posts})

class ItemsView(APIView):
    def get(self, request):
        location_id = request.query_params.get('location_id')
        print("location_id: " + str(location_id))
        items = None
        if location_id:
            items = Item.objects.filter(location__id = location_id)
        else:
            items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
