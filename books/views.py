# @api_view(['GET'])
# def get_all_books(request):
#     try:
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
#     except Author.DoesNotExist:
#         return Response({"error": "No authors found"}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @api_view(['GET', 'PUT', 'DELETE'])
# def author(request, pk):
#     try:
#         author = Author.objects.get(pk=pk)
#         if request.method == 'GET':
#             serializer = AuthorSerializer(author)
#             return Response(serializer.data)
#         elif request.method == 'PUT':
#             serializer = AuthorSerializer(author, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors)
#         else:
#             author.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#     except:
#         return Response({"error": "Author not exist"}, status=status.HTTP_404_NOT_FOUND)

from rest_framework.views import APIView
from .models import Author
from rest_framework import status
from authors.models import Author
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import BookSerializer
from .models import Book

def get_author_by_pk(pk):
    try:
        return Author.objects.get(pk=pk)
    except:
        return Response({
            'error': 'Author not found'
        }, status=status.HTTP_404_NOT_FOUND)

class BookList(APIView):
    def get(self, request):
        Books = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    
class BookCreate(APIView):
        author = get_author_by_pk(request.data["author"])
        if author:
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({"error": "Author does not found"}, status=status.HTTP_404_NOT_FOUND)
        
class BookDetail(APIView):
    def get_Book_by_pk(self, pk):
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