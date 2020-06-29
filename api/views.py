from api.models import Posts_Review
from rest_framework.viewsets import ModelViewSet
from api.serializers import Posts_ReviewSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class PostsReviewViewSet(ModelViewSet):
    serializer_class = Posts_ReviewSerializer
    basename = 'posts_review'
    queryset = Posts_Review.objects.all().order_by('-time')

    @action(detail=True, methods=['get'])
    def up_vote(self, request, pk=None):
        get_posts = self.get_object()
        get_posts.up_votes += 1
        get_posts.save()
        return Response({'status': 'vote increase'})

    @action(detail=True, methods=['get'])
    def down_votes(self, request, pk=None):
        get_posts = self.get_object()
        get_posts.down_votes += 1
        get_posts.save()
        return Response({'status': 'vote decrease'})


class BoastViewSet(ModelViewSet):
    serializer_class = Posts_ReviewSerializer
    basename = 'boast'
    queryset = Posts_Review.objects.filter(is_boast=True)


class RoastViewSet(ModelViewSet):
    serializer_class = Posts_ReviewSerializer
    basename = 'Roast'
    queryset = Posts_Review.objects.filter(is_boast=False)




















