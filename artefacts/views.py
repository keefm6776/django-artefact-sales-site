from django.shortcuts import render
from .models import Artefact

# Create your views here.

def all_artefacts(request):
    artefacts = Artefact.objects.all()
    return render(request, "artefacts.html", {"artefacts": artefacts})
