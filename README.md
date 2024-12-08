# codeflix-catalog-admin
Administração de Catálogo – Codeflix - Python

## Running

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
docker run -d --hostname rabbitmq --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
python manage.py startconsumer
python manage.py runserver
```


## Regras Category
- [x] Nome da categoria deverá ser obrigatório.
- [x] Nome deverá ter no máximo 255 caracteres.
- [x] Ao criar uma nova categoria um identificador deve ser gerado no formato (uuid).
- [x] Ao criar uma categoria os campos id, descrição e isActive não serão obrigatórios.
- [x] Caso a propriedade isActive não seja informada, deverá receber como default o valor true.
- [ ] Teste __str__ - Exercício
- [ ] Teste __repr__ - Exercício



