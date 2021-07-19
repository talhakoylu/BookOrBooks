from rest_framework import status
from rest_framework.response import Response
from account.api.serializers.register_serializers import ChangePasswordSerializer
from utils.general_permissions import NotAuthenticated
from rest_framework.generics import CreateAPIView, UpdateAPIView
from django.contrib.auth import get_user_model, update_session_auth_hash
from account.api.serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class CreateUserAPIView(CreateAPIView):
    model = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [NotAuthenticated]

class PasswordUpdateAPIView(UpdateAPIView):
    model = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data = request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully."
            }
            update_session_auth_hash(request, self.object)
            return Response(response)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

