from ..models import *
import random
import csv
from io import TextIOWrapper, StringIO
from django.shortcuts import render

class FruitsService:
    '''
    フルーツサービス
    '''
    def __init__(self, request):
        '''
        コンストラクタ
        '''
        self.request = request

    def get_fruitslist(self):
        '''
        フルーツリストを取得
        '''
        fruits_list = Fruits.objects.all()
        return fruits_list

    def get_randam_fruitslist(self):
        '''
        フルーツリストランダム取得
        '''
        fruits_num = self.get_numrecord()
        random_num = random.randrange(fruits_num)
        fruits_list = Fruits.objects.all()[:random_num]
        return fruits_list

    def get_numrecord(self):
        '''
        フルーツのレコード数取得
        '''
        fruits_num = Fruits.objects.all().count()
        return fruits_num

    def upload(request):
        if 'csv' in request.FILES:
            form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
            csv_file = csv.reader(form_data)
            for line in csv_file:
                fruits, created = Fruits.objects.get_or_create(name=line[1])
                fruits.name = line[0]
                fruits.memo = line[1]
                fruits.save()
            return render(request, 'kadai/upload.html')
        else:
            return render(request, 'kadai/upload.html')
