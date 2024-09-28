from datetime import date # importa a classe date
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_list_or_404, get_object_or_404
# from django.template import loader
from django.urls import reverse

# from agenda.models import eventos
from agenda.models import Evento


# Create your views here.
def listar_evento(request):
    # Buscar os eventos criados no Banco de Dados
    # Exibir um template listando esses eventos
    eventos = Evento.objects.filter(data__gte=date.today())
    
    # Organiza os eventos por data
    eventos = sorted(eventos, key=lambda e: e.data)
    
    return render(
        request=request,
        context={'eventos': eventos},
        template_name='agenda/listar_eventos.html'
    )



def exibir_evento(request, id): # /eventos/1/
    # evento = {
    #     "nome": "Aula de Python",
    #     "categoria": "Backend",
    #     "local": "Rio de Janeiro"
    # }

    # evento = eventos[1] # pega o evento da lista
    # template = loader.get_template('agenda/exibir_evento.html') # carrega o template
    # rendered_template = template.render(context={'evento': evento}, request=request) # renderiza o template, e retorna uma string HTML

    evento = Evento.objects.get(id=id)
    if not evento:
        evento = get_object_or_404(Evento, id=id)
    
    
    # return HttpResponse(rendered_template) # retorna a string HTML

    # --- OU ---
    return render(
        request=request,
        context={'evento': evento},
        template_name='agenda/exibir_evento.html'
    )
    
    
    
def participar_evento(request):
    evento_id = request.POST.get('evento_id')
    evento = get_object_or_404(Evento, id=evento_id)
    evento.participantes += 1
    evento.save() # depois de atualizar o evento, salva no BD
    
    # uma boa prática quando estiver lidando com forms em HTML, sempre redirecionar o usuário para uma nova página que faça um request GET normalmente, e não um POST, para que o usuário acabe mudando dados não intencionadamente na aplicação
    # return HttpResponseRedirect(f"/eventos/{evento.id}/")
    # --- OU ---
    return HttpResponseRedirect(reverse('exibir_evento', args=(evento_id,)))