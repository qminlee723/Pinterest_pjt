from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == 'POST':
        # request에서 POST 메서드 중, `hello_world_input`이라는 이름의 데이터를 가져와서 temp에 할당해라
        temp = request.POST.get('hello_world_input')

        # HelloWorld 빵틀(모델)에서 나온 새로운 객체가 new_hello_world에 할당됨
        new_hello_world = HelloWorld()
        # HelloWorld의 text라는 속성값이 존재함. 여기에 우리가 받는 input을 넣어줌
        new_hello_world.text = temp
        # DB에  저장
        new_hello_world.save()

        context = {'text': temp, 'hello_world_output': new_hello_world,}
        return render(request, 'accountapp/hello_world.html', context)
    else:
        context={'text': 'GET METHOD!!!'}
        return render(request, 'accountapp/hello_world.html', context)