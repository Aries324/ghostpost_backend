from api.models import Posts_Review
from rest_framework.viewsets import ModelViewSet
from api.serializers import Posts_ReviewSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class PostsReviewViewSet(ModelViewSet):
    serializer_class = Posts_ReviewSerializer
    basename = 'posts_review'
    queryset = Posts_Review.objects.all()

    @action(detail=True, methods=['post'])
    def up_vote(self, request, pk=None):
        get_posts = Posts_Review.objects.get(pk=pk)
        get_posts.up_votes += 1
        get_posts.save()
        return Response({'status': 'vote decrease'})

        # return Response({
        #     'pk': get_posts.pk,
        #     'up_votes': get_posts.up_votes
        # })

    @action(detail=True, methods=['post'])
    def down_votes(self, request, pk=None):
        get_posts = Posts_Review.objects.get(pk=pk)
        get_posts.down_votes -= 1
        get_posts.save()
        return Response({'status': 'vote decrease'})



