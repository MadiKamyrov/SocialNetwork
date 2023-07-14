from rest_framework import viewsets, permissions, generics, status, exceptions
from rest_framework.response import Response

from .models import User, Post, Like
from .serializers import UserSerializer, PostSerializer, LikeSerializer
from .permissions import IsAuthor, IsOwnerOrReadOnly


# Create your views here.

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthor]


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        post_id = request.data.get('post')
        user = request.user

        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response({"detail": "Post does not exist."}, status=status.HTTP_404_NOT_FOUND)

        if Like.objects.filter(user=user, post=post).exists():
            raise exceptions.ValidationError("You have already liked this post.")

        like = Like(user=user, post=post)
        like.save()

        return Response(LikeSerializer(like).data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.user != request.user:
            return Response({"detail": "You are not the owner of this like."}, status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
