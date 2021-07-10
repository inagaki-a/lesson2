from django import forms

class FruitsForm(forms.Form):
    '''
    フルーツフォーム
    '''
    id = forms.IntegerField(label='№')
    name = forms.CharField(label='果物名', max_length=100)
    memo = forms.CharField(label='メモ', max_length=200)
    