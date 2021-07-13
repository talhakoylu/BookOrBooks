from utils.general_permissions import NotAuthenticated
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from account.api.serializers import RegisterSerializer


User = get_user_model()

class CreateUserAPIView(CreateAPIView):
    model = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [NotAuthenticated]