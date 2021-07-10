from django import views
from django.shortcuts import render
from django.views.generic.base import View
from kadai504.forms.kadai504.create_form import FruitsForm
from django.views.generic import TemplateView
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

class Fruits:
    '''
    フルーツクラス
    '''
    fruits_list =[]

    def __init__(self, id, name, memo):
        '''
        コンストラクタ
        '''
        self.id = id
        self.name = name
        self.memo = memo

    def add_fruits(self, fruits):
        '''
        果物を追加
        '''
        Fruits.fruits_list.append(fruits)

    def get_fruits(self, id):
        '''
        果物を取得する
        '''
        for fruits in Fruits.fruits_list:
            if int(fruits.id) == int(id):
                return fruits
                break

    def delete_fruits(self, id):
        '''
        フルーツを削除する
        '''
        for fruits in Fruits.fruits_list:
            if int(fruits.id) == int(id):
                Fruits.fruits_list.remove(fruits)
                
class FruitsList(View):
    '''
    フルーツリストクラス
    '''
    def get(self, request):
        Fruits.fruits_list
        params = {
            'fruits_list' : Fruits.fruits_list, 
        }
        return render(request, 'kadai504/list.html', params)

class FruitsCreate(View):
    '''
    フルーツ作成クラス
    '''
    def get(self, request):
        '''
        フルーツ登録画面初期表示
        '''
        params = {
            'form':FruitsForm()
        }
        return render(request, 'kadai504/create.html', params)

    def post(self, request, *args, **kwargs):
        '''
        フルーツ登録処理
        '''
        id = request.POST['id']
        name = request.POST['name']
        memo = request.POST['memo']
        #同じＩＤがあったらＮＧ処理必要
        fruits = Fruits(id, name, memo)
        Fruits.add_fruits(request, fruits)
        return redirect(reverse('kadai504:fruits_list_view'))

class FruitsDelete(View):
    '''
    フルーツ削除
    '''
    def get(self, request, *args, **kwargs):
        '''
        フルーツ削除画面初期表示
        '''
        id = kwargs.get('id')
        fruits = Fruits.get_fruits(request, id)
        '''
        initial_dict = {
            'id': fruits.id,
            'name': fruits.name,
            'memo': fruits.memo,
        }
        '''
        params = {
            #'form':FruitsForm(initial=initial_dict),
            'fruits':fruits,
        }
        return render(request, 'kadai504/delete.html', params)

    def post(self, request, *args, **kwargs):
        '''
        フルーツ削除実行
        '''
        id = kwargs.get('id')
        Fruits.delete_fruits(request, id)
        return redirect(reverse('kadai504:fruits_list_view'))



#フルーツリストのインスタンスを作成
#登録更新画面でNo,name,memoを入力して登録時にフルーツインスタンスを作成してフルーツリストに追加
#リストを呼出すとフルーツリストのインスタンスのリストを表示する
