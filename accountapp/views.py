from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import HelloWorld

# Create your views here.
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

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        context = {
            'hello_world_list': hello_world_list,
        }
        return render(request, 'accountapp/hello_world.html', context)


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'
