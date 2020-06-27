from rest_framework.serializers import HyperlinkedModelSerializer

from api.models import Posts_Review

class Posts_ReviewSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Posts_Review
        fields = (
            'is_boast',
            'content',
            'up_votes',
            'down_votes',
            'time'
        )
