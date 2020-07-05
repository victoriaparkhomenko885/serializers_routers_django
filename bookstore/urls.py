from django.urls import path, include

from .routers import router
from .views import AuthorList, AuthorDetail


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('author/', AuthorList.as_view()),
    path('author/<int:pk>/', AuthorDetail.as_view())
]
