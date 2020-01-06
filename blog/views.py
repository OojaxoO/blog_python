from blog.models import Blog
from rest_framework import viewsets
from blog.serializers import BlogSerializer 

# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer 
