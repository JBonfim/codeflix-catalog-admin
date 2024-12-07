Comandos:

act -l  
act -j tests

# docker:
docker run -it ubuntu:latest /bin/bash

# Git:
git fetch --all
git reset --soft HEAD~1
git checkout main -- .\deployment\inventory\group_vars\secrets_homolog.yml

CHMOD:
chmod +x .\build_lambda.sh

# Angular:
npm i --legacy-peer-deps

# Python: 
python3 -m venv venv

source venv/bin/activate ou .\venv\Scripts\Activate
Comando + k = clear no terminal


pip freeze # verifica as bibliotecas instaladas.



- Visualizar estrutura do projeto:
  - tree .\src\ | Select-String -Pattern '__pycache__' -NotMatch


Utilizei o pytest e unittest

1) .\venv\Scripts\Activate
2) python
3) Exemplo:  
import django
print(django.get_version())

- Rodar o django
  - python manage.py
  - python manage.py runserver

mkdir -p src/django_project\category_app
python manage.py startapp category_app .\src\django_project\category_app

# Migration
 - python manage.py makemigrations # criar migrations com django
 - python manage.py migrate # cria/atualiza a tabela
 - python manage.py dbshell
 - python manage.py createsuperuser

# Rodar Testes:
python manage.py test django_project

# Dependencias:
- pip install pytest
- pip install django
- pip install djangorestframework
- pip install pytest-django