from account.api.permissions import IsParent
from account.api.serializers.child_list_serializers import ChildListSerializer, ChildRecordAddSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
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
