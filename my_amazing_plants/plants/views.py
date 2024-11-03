from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from .models import Plant
from .forms import PlantForm # type: ignore

# List view
def plant_list(request):
    plants = Plant.objects.all()
    return render(request, 'plants/plant_list.html', {'plants': plants})

# Create view
def plant_create(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('plant_list')
    else:
        form = PlantForm()
    return render(request, 'plants/plant_form.html', {'form': form})

# Update view
def plant_update(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_list')
    else:
        form = PlantForm(instance=plant)
    return render(request, 'plants/plant_form.html', {'form': form})

# Delete view
def plant_delete(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    if request.method == 'POST':
        plant.delete()
        return redirect('plant_list')
    return render(request, 'plants/plant_confirm_delete.html', {'plant': plant})

def plant_trade(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    # Add logic for trading the plant
    # For example, you might want to redirect to a trade confirmation page or process the trade here

    # Example response (replace with your logic):
    return render(request, 'plants/plant_trade_confirmation.html', {'plant': plant})