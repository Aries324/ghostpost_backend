from django.conf.urls import include, url

from api.views import PostsReviewViewSet, BoastViewSet, RoastViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'post_review', PostsReviewViewSet, basename='post_review')
router.register(r'boasts', BoastViewSet, basename='roasts')
router.register(r'roasts', RoastViewSet, basename='roasts')
# router.register(r'create_post', CreatePost, basename='create_post')

urlpatterns = [
    url(r'^api/', include(router.urls))

]
