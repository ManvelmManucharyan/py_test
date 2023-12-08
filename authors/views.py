from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializer
from rest_framework import status

class AuthorList(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    
class AuthorCreate(APIView):
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class AuthorDetail(APIView):
    def get_author_by_pk(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Author not found'
            }, status=status.HTTP_404_NOT_FOUND)
            
    def get(self, request, pk):
        author = self.get_author_by_pk(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    
    def put(self, request, pk):
        author = self.get_author_by_pk(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
        
    def delete(self, request, pk):
        author = self.get_author_by_pk(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)