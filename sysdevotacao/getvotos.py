from models import turmas


for itens in turmas.objects.all():
    print(itens)