from django.urls import path
from .views import *

urlpatterns = [
    path(
        "resources/",
        ListAllResourcesView.as_view(),
        name="list_all_resources"
    ),
    path(
        "resources/create/",
        CreateResourceView.as_view(),
        name="create_resource"
    ),
    path(
        "resources/<int:pk>/update/",
        UpdateResourcesView.as_view(),
        name="update_resource"
    ),
    path(
        "resources/<int:pk>/delete",
        DeleteResourceView.as_view(),
        name="delete_resource"
    )

]
