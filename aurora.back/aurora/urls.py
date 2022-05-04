from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("aurora.drf.urls", namespace="api")),
    path("docs/", include_docs_urls(title="AuroraAPI")),
    path(
        "schema",
        get_schema_view(
            title="AuroraAPI",
            description="This is a kind of documentation for my Aurora project.",
            version="1.0.0",
        ),
        name="openapi-schema",
    ),
]
