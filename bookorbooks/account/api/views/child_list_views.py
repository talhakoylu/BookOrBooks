from account.models.parent_profile_model import ParentProfile
from account.api.permissions import IsParent
from account.api.serializers.child_list_serializers import ChildListSerializer, ChildRecordAddSerializer, ParentSerializerNew
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, get_object_or_404
from account.models import ChildList
from rest_framework.permissions import IsAuthenticated

class ChildListAPIView(ListAPIView):
    queryset = ChildList.objects.all()
    serializer_class = ChildListSerializer


class ChildListCreateAPIView(CreateAPIView):
    queryset = ChildList.objects.all()
    serializer_class = ChildRecordAddSerializer
    permission_classes = [IsAuthenticated, IsParent]

    def perform_create(self, serializer):
        serializer.save(parent=self.request.user.user_parent_profiles)


class ChildListByUserAPIView(RetrieveAPIView):
    queryset = ParentProfile.objects.all()
    serializer_class = ParentSerializerNew
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(ParentProfile, user=self.request.user.id)
        return obj