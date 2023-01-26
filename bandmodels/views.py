from .forms import BandFormMain, BandForm
from bandmodels.data.notebooks import dex as dex
from django.shortcuts import render
from .models import BandResults

# dexmodel
dex_model = dex.DEXModel("bandmodels/data/notebooks/band.xml")

# Create your views here.


def home_view(request):
    form = BandFormMain(
        dex_model.get_input_attributes_detailed())
    return render(request, "home.html", {"form": form})


def dex_model_view(request):
    if request.method == "POST":
        form = BandForm(dex_model.get_input_attributes(), request.POST)
        if form.is_valid():
            eres, qq_res = dex_model.evaluate_model(form.cleaned_data)
            for k, v in qq_res.items():
                if k == "Choosing a band":
                    dex_ocena = v
            if request.POST.get("name"):
                name = request.POST.get("name")
            else:
                name = "Neznani band"
            band = BandResults(name=name, dex_ocena=dex_ocena)
            band.save()

            context = {"eres": eres, "qq_res": qq_res, "name": name}
            return render(request, "dex_results.html", context)
    else:
        form = BandForm(dex_model.get_input_attributes())
    return render(request, "home.html", {"form": form})


def band_list_view(request):
    objects = BandResults.objects.all()

    context = {
        "band_objects": objects,
    }
    return render(request, "band_list.html", context=context)
