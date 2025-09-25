from rest_framework import generics, permissions
from .serializers import ResourceSerializer
from .models import Resource
# Create your views here.

class ListAllResourcesView(generics.ListAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Exact match filtering (e.g., /api/resources/?category=web_app_security)
    filterset_fields = ["category"]

    # Search across fields (e.g., /api/resources/?search=security)
    search_fields = ["title", "description"]

    # Ordering (e.g., /api/resources/?ordering=title or /api/resources/?ordering=id
    ordering_fields = ["title", "id"]
    ordering = ["id"]  # default ordering

class CreateResourceView(generics.CreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permissions = [permissions.IsAuthenticated]

class UpdateResourcesView(generics.UpdateAPIView):
    """
    API endpoint to update an existing Resource.
    Supports PUT (full update) and PATCH (partial update).
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeleteResourceView(generics.DestroyAPIView):
    """
    API endpoint to delete a Resource.
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticated]