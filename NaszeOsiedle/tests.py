from unittest.mock import ANY

import pytest
from django.test import TestCase
from rest_framework.test import APIClient
# Create your tests here.
from NaszeOsiedle.models import Inhabitant

inhabitant = APIClient()

@pytest.mark.django_db
def test_LoginView():
    citizen = Inhabitant.objects.create(**{
        "user_name": "502/2",
        "first_name": "Filip",
        "last_name": "Konopka",
        "e_mail": "filip.konopka88@gmail.com",
        "flat_area": 52.88,
    })
    citizen.set_password("P@ssword123")
    citizen.save()
    jwt = inhabitant.post('/login', data={
        "user_name": "502/2",
        "password": "P@ssword123"
    })
    assert jwt.json() == {"jwt": ANY}

    wrong_password = inhabitant.post('/login', data={
        "user_name": "502/2",
        "password": "P@sswo"})
    assert wrong_password.status_code == 403
    assert wrong_password.json().get('detail') == "Nie prawidlowe dane do logowania"

# @pytest.mark.django_db
# def test_LogoutUserView():
#     logout_user = client.get('/logout')
#     assert logout_user.json().get('message') == "Wylogowany"