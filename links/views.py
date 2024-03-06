from .models import ShortLink
from .serializers import ShortLinkSerializer
from django.shortcuts import get_object_or_404
from django.db.models import F
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


class ShortLinkView(generics.CreateAPIView):
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkSerializer
    permission_classes = [AllowAny]


@api_view(["PUT"])
@csrf_exempt
def short_to_long_link(request, short_link):
    link = get_object_or_404(ShortLink, short_link=short_link)
    ShortLink.objects.filter(short_link=short_link).update(
        visit_number=F("visit_number") + 1
    )
    serializer = ShortLinkSerializer(link)
    return Response(serializer.data)
