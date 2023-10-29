from django.shortcuts import render
from .models import Article,Product
from .serializers import ArticleSerializer,ProductSerializer
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    return HttpResponse('hi man')

def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializers = ArticleSerializer(articles,many=True)
        return JsonResponse(serializers.data,safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = ArticleSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data,status=201)
        return JsonResponse(serializers.errors,safe=False,status=404)
@csrf_exempt  
def product_list(request):
    if request.method == 'GET':
        articles = Product.objects.all()
        serializers = ProductSerializer(articles,many=True)
        return JsonResponse(serializers.data,safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = ProductSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data,status=201)
        return JsonResponse(serializers.errors,safe=False,status=404)
       

@csrf_exempt
def select_product_list(request,pk):
    try:
        article = Product.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializers = ProductSerializer(article)
        return JsonResponse(serializers.data)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = ProductSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data,status=201)
        return JsonResponse(serializers.errors,safe=False,status=401)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializers = ProductSerializer(article,data=data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data,status=200)
        return JsonResponse(serializers.errors,safe=False,status=400)
    if request.method == 'DELETE':
        article.delete()
        return HttpResponse(200)
    




