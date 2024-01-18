from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from .models import User
from django.contrib import messages
from django.contrib.messages import constants
import re
from django.contrib import auth


def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/imobi')
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('senha')

        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Ops! Por favor preencha os campos corretamente!')
            return redirect('/imobi/cadastro')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Ops! Já existe um usuário com este nome no sistema!')
            return redirect('/imobi/cadastro')
        
        email = User.objects.filter(email=email)

        if email.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com este email no sistema!')
            return redirect('/imobi/cadastro')
        
        if len(password.strip()) < 8:
            messages.add_message(request, constants.ERROR, 'Sua senha deverá ter no mínimo 8 caracteres!')
            return redirect('/imobi/cadastro')
        
        if not re.search('[A-Z]', password):
            messages.add_message(request, constants.WARNING, 'Sua senha deve conter pelo menos 1 letra maiúscula, 1 letra minúscula e números!')
            return redirect('/imobi/cadastro')
        if not re.search('[a-z]', password):
            messages.add_message(request, constants.WARNING, 'Sua senha deve conter pelo menos 1 letra maiúscula, 1 letra minúscula e números!')
            return redirect('/imobi/cadastro')
        if not re.search('[1-9]', password):
            messages.add_message(request, constants.WARNING, 'senha deve conter pelo menos 1 letra maiúscula, 1 letra minúscula e números!')
            return redirect('/imobi/cadastro')

        try:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastro com sucesso!')
            return redirect('/imobi/logar')
        
        except Exception as error:
            messages.add_message(request, constants.ERROR, f'O erro encontrado foi {error.__class__}')
            return redirect('/imobi/cadastro')
        except Exception as causa:
            messages.add_message(request, constants.ERROR, f'O erro encontrado foi {causa.__cause__}')
            return redirect('/imobi/cadastro')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema!')
            return redirect('/imobi/cadastro')


def logar(request):
    if request.user.is_authenticated:
        return redirect('/imobi')
    if request.method == "GET":
        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('senha')
        
        user = auth.authenticate(username=username, password=password)

        if not user:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos!')
            return redirect('/imobi/logar')
        else:
            auth.login(request, user)
            return redirect('/home')
        

def sair(request):
    auth.logout(request)
    return redirect('/imobi/logar')



        