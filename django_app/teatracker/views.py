from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item, Entry, Location
from .serializers import ItemSerializer, LocationSerializer
from .forms import LocationForm

def main(request):
    return render(request, "teatracker/main.html")

def entry_overview(request):
    entries = Entry.objects.all()
    return render(request, "teatracker/entry_overview.html", {"entries": entries})
# def tea_entry(request):
#     locations = None
#     items = None# load all items
#     return render(request, 'blog/blog_home.html', {"posts": posts})

def new_entry_location(request):
    locations = Location.objects.all()
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            location.save()
            # return redirect('post_detail', pk=post.pk)
    
    location_form = LocationForm()
    return render(
        request, 
        "teatracker/new_entry_location.html", 
        {
            "locations": locations,
            "location_form": location_form,
        }
    )

def new_entry_items(request, location_id):
    items = Item.objects.filter(location__id = location_id)
    return render(request, "teatracker/new_entry_items.html", {"items": items})

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

class LocationsView(APIView):
    def get(self, request):
        location_id = request.query_params.get('location_id')
        if location_id:
            location = Location.objects.filter(id = location_id)
            serializer = LocationSerializer(location, many=True)
            return Response(serializer.data)
        else:
            locations = Location.objects.all()
            serializer = LocationSerializer(locations, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)