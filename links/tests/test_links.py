import pytest
from django.urls import reverse

long_link = "http://MVSXX.COMPANY.COM:04445/CICSPLEXSM//JSMITH/VIEW/OURLOCTRAN?CONTEXT=FRED&SCOPE=FRED&A_TRANID=PAY*"


@pytest.mark.django_db
@pytest.mark.parametrize("link", ("http://example.com", long_link, "http://x.pl"))
def test_short_link_view_create_short_link(client, link):
    data = {}
    data["link"] = link
    response = client.post(reverse("short_link"), data=data)
    assert response.data.get("link") == link
    assert "short_link" in response.data


@pytest.mark.django_db
@pytest.mark.parametrize("link", ("abc", "htttp://example.com", "http://x y.pl"))
def test_short_link_viwe_return_wrong_url(client, link):
    data = {}
    data["link"] = link
    response = client.post(reverse("short_link"), data=data)
    assert response.data.get("link")[0] == "Enter a valid URL."


@pytest.mark.django_db
@pytest.mark.parametrize("link", ("http://example.com", long_link, "http://x.pl"))
def test_same_link_retunrn_same_short_link(client, link):
    data = {}
    data["link"] = link
    response1 = client.post(reverse("short_link"), data=data)
    response2 = client.post(reverse("short_link"), data=data)
    assert response1.data.get("link") == link
    assert response2.data.get("link") == link
    assert response1.data.get("short_link") == response2.data.get("short_link")


@pytest.mark.django_db
@pytest.mark.parametrize("link", ("http://example.com", long_link, "http://x.pl"))
def test_short_to_long_return_correct_long_link(client, create_short_link, link):
    short_link = create_short_link(link)
    response = client.put(reverse("short_to_long_link", args=[short_link]))
    print(response)
    assert response.data.get("link") == link


@pytest.mark.django_db
@pytest.mark.parametrize("short_link", ("dseax", "grsrt", "loaie"))
def test_wrogn_short_link_return_404(client, short_link):
    response = client.put(reverse("short_to_long_link", args=[short_link]))
    assert response.status_code == 404
