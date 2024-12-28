import pytest
import requests



@pytest.fixture(scope="function")
def get_joke():
    get_joke = requests.get(" https://geek-jokes.sameerkumar.website/api").text
    return get_joke.rstrip()