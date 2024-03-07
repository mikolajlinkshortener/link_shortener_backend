import pytest
from django.test import RequestFactory
from links.serializers import ShortLinkSerializer


def make_short_link(long_link):
    data={"link": long_link}
    request = RequestFactory()
    request.META = {}
    link_serializer = ShortLinkSerializer(data=data, context={'request': request})
    link_serializer.is_valid()
    link = link_serializer.save()
    return link.short_link


@pytest.fixture
def create_short_link():
    return make_short_link
