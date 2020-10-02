from rest_framework import viewsets
from articles.api.serializers import ArticleSerializer
from articles.models import Article


class ArticleViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
# from rest_framework import generics
# from articles.api.serializers import ArticleSerializer
# from articles.models import Article


# class ArticleListView(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class ArticleCreateView(generics.CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class ArticleUpdateView(generics.CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class ArticleDeleteView(generics.CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
