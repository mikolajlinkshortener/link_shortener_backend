from rest_framework import serializers
from .mixin import ModelSerializerDefaultsMixin
from .models import ShortLink
from .permutation_generator import Permutation


class ShortLinkSerializer(ModelSerializerDefaultsMixin, serializers.ModelSerializer):
    short_link = serializers.CharField(required=False)

    class Meta:
        model = ShortLink
        fields = ["link", "short_link"]

    def create(self, validated_data):
        shortened = "".join(next(Permutation.short_link_generator))
        short_link, created = ShortLink.objects.get_or_create(
            link=validated_data.get("link")
        )
        if created:
            short_link.short_link = shortened
        short_link.save()
        return short_link
