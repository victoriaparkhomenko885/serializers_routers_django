from rest_framework import routers

from . import views

router = routers.DefaultRouter()


router.register('book', views.BookViewSet)
router.register('publisher', views.PublisherViewSet)
