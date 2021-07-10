from django.shortcuts import render
from django.views import View
# Create your views here.
from .service.fruits_service import *
from django.core.paginator import PageNotAnInteger, Paginator
from django.views.generic.list import ListView

class HelloView(View):
    '''
    ハローワールド
    '''
    def get(self, request):
        '''
        現在時刻と日付の表示
        '''
        return render(request, 'kadai/helloworld.html')

class FruitsView(View):
    '''
    フルーツ
    '''
    def get(self, request):
        '''
        フルーツリストを表示する
        '''
        #503_02
        fruits_list = FruitsService(request).get_fruitslist()
        #503_03
        #fruits_list = FruitsService(request).get_randam_fruitslist()
        #503_04
        pagenator = Paginator(fruits_list, 1) #1ページに20件
        page = request.GET.get('page')#urlのパラメーターからの現在のページ番号を取得
        print(page)
        fruits_list = pagenator.get_page(page)#指定のページのフルーツを取得
        params = {
            'fruits_list' : fruits_list, 
        }
        return render(request, 'kadai/list.html', params)

#簡単version
class IndexView(ListView):
    model = Fruits
    template_name = 'kadai/list.html'
    paginate_by = 8