# Ici j'importe les fonctions qui pourront me servir dans la création de mes vues depuis Django

from django.shortcuts import render
from django.shortcuts import redirect

# Ici j'importe mon modèle

from RailExpress.models import trains

# Create your views here.
    

# Ici je crée ma première vue pour ma page d'accueil
def index(request):

    # Ici je vérifie d'abord que la recherche a été soumise avec ma condition
    if 'search-input' in request.GET:

    # Ici je vais récupérer la valeur qui sera entrée dans la recherche qui sera l'ID d'un train
        search_input = request.GET['search-input'] 

    # Ici avec "return redirect" je vais rediriger l'utilisateur vers ma vue show qui sera ma page pour les détails suivi de l'ID du train entré dans la barre de recherche    
        return redirect('show', ID_Train=search_input)
    
    #Ici je vais récupérer tous les trains présents dans ma base de données
    MesTrains = trains.objects.all()

    #Ici je vais sélectionner aléatoirement un train présent dans ma base de données
    random_train = trains.objects.order_by('?').first()

    #Là avec "return render" je vais renvoyer ma page index.html
    return render(request, "RailExpress/index.html", {
        'MesTrains' : MesTrains,
        'randomTrain' : random_train.IDTrain
    })

#Ici je crée ma seconde vue pour afficher les détails d'un train en particulier
def show(request, ID_Train) : 

    #Ici je récupère l'ID du train depuis la base de données
    TousNosTrains = trains.objects.get(IDTrain = ID_Train)

    #Ici je stocke les détails du train récupérés dans une variable pour pouvoir l'utiliser facilement après
    MonPremierTrain = TousNosTrains

    #Là avec "return render" je renvoie ma page show.html avec les détails du train
    return render (request, "RailExpress/show.html", {
        "ID_train" : MonPremierTrain.IDTrain,
        "Plan" : MonPremierTrain.Plan,
        "Destination" : MonPremierTrain.Destination,
        "Datetime" : MonPremierTrain.Datetime,
        "Description" : MonPremierTrain.Description,
        "Cover" : MonPremierTrain.Cover

    })
