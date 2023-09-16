import debug_toolbar

from django.urls import include, path

from .urls import urlpatterns

urlpatterns += [
    path("__debug__/", include(debug_toolbar.urls)),
]
