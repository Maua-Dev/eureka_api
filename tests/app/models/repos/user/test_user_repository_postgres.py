import datetime

from django.test import TransactionTestCase

from app.models import User
from app.repos.user.user_repository_postgres import UserRepositoryPostgres


class TestUserRepositoryPostgres(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        User.objects.create(user_id=0, name="Vitor Soller")
        User.objects.create(user_id=1, name="Brancas")
        User.objects.create(user_id=2, name="Hector Guerrini")
        User.objects.create(user_id=3, name="Bruno Vilas")
        User.objects.create(user_id=4, name="Luigi Televisão")

    def tearDown(self):
        User.objects.all().delete()

    def test_get_user(self):
        repo = UserRepositoryPostgres()
        user = repo.get_user(1)
        assert user["user_id"] == 1
        assert user["name"] == "Brancas"
        
    def test_get_user_not_found(self):
        repo = UserRepositoryPostgres()
        user = repo.get_user(100)
        assert user is None
