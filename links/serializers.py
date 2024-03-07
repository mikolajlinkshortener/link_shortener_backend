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
        short_link, created = ShortLink.objects.get_or_create(
            link=validated_data.get("link")
        )
        if created:
            shortened = "".join(next(Permutation.short_link_generator))
            request = self.context.get("request")
            print(request)
            short_link.short_link = shortened
            short_link.ip = self.get_client_ip(request)
            short_link.user_agent = request.META.get("HTTP_USER_AGENT", '')
            short_link.save()
        return short_link

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR",'')
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR", '')
        return ip
