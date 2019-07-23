from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from . import models
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def all_post(request):
    all_posts = models.Post.objects.all()
    all_posts_serialized = serializers.serialize('json', all_posts)
    all_posts_json = json.loads(all_posts_serialized)
    data = json.dumps(all_posts_json)
    return HttpResponse(data)


@csrf_exempt
def insert_post(request):
    post_instance = models.Post()
    post_instance.title = request.POST['title']
    post_instance.description = request.POST['description']
    post_instance.author = models.Author.objects.all()[0]
    post_instance.save()

    return HttpResponse("200")


def test(request):
    return HttpResponse("Welcoooooooome")
