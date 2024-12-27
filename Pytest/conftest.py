import pytest
from faker import Faker
import requests



faker = Faker()

@pytest.fixture()
def get_joke():
    get_joke = requests.get(" https://geek-jokes.sameerkumar.website/api").text
    return get_joke