from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


# getting all books
@api_view(['GET'])
def Booklist(request):
    booksobj=BooksModel.objects.all()#query set
    serializer=BookSerializer(booksobj,many=True)
    return Response(serializer.data)


# create new book
@api_view(['POST'])
def post_Book(request):
    booksobj=BooksModel.objects.all()#query set
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# update book
@api_view(['POST'])
def update_Book(request,id):
    booksobj=BooksModel.objects.get(id=id)#query set
    serializer=BookSerializer(instance=booksobj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# delete book
@api_view(['DELETE'])
def delete_Book(request,id):
    booksobj=BooksModel.objects.get(id=id)#query set
    booksobj.delete()
    return Response("Book is deleted")