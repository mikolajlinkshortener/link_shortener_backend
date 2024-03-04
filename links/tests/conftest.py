import pytest
from links.serializers import ShortLinkSerializer


def make_short_link(long_link):
    link_serializer = ShortLinkSerializer(data={"link": long_link})
    link_serializer.is_valid()
    link = link_serializer.save()
    return link.short_link


@pytest.fixture
def create_short_link():
    return make_short_link
