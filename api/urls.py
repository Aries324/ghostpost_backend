from django.conf.urls import include, url

from api.views import PostsReviewViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'post_review', PostsReviewViewSet, basename='post_review')


urlpatterns = [
    url(r'^api/', include(router.urls))

]
