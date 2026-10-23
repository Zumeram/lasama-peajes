from django.shortcuts import render, redirect, get_object_or_404
from .models import Viaje, Peaje
from django.utils import timezone
from django.db.models import Sum
import random, string
from datetime import date

def generar_codigo():
    fecha = date.today().strftime("%Y%m%d")
    correlativo = Viaje.objects.filter(codigo__contains=fecha).count() + 1
    return f"LASAMA-RENG-CHIL-{fecha}-{correlativo:03d}"

# VISTA 1: CHOFERES - /  (solo móvil)
def lista_choferes(request):
    viajes = Viaje.objects.filter(finalizado=False).order_by('-fecha_inicio')
    return render(request, 'viajes/lista.html', {'viajes': viajes})

# VISTA 2: FINANZAS - /finanzas/  (dashboard con datos REALES, parte en 0)
def dashboard_finanzas(request):
    viajes = Viaje.objects.all().order_by('-fecha_inicio')
    hoy = timezone.now()
    inicio_mes = hoy.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    
    total_mes = Peaje.objects.filter(viaje__fecha_inicio__gte=inicio_mes).aggregate(Sum('monto'))['monto__sum'] or 0
    peajes_validados = Peaje.objects.count()
    viajes_activos = Viaje.objects.filter(finalizado=False).count()
    barcazas = Peaje.objects.filter(tipo='BARCAZA').count()
    
    context = {
        'viajes': viajes,
        'total_mes': total_mes,
        'peajes_validados': peajes_validados,
        'viajes_activos': viajes_activos,
        'barcazas': barcazas,
    }
    return render(request, 'viajes/finanzas.html', context)

def iniciar_viaje(request):
    if request.method == "POST":
        origen = request.POST.get("origen","").strip()  # ← AHORA EN BLANCO
        destino = request.POST.get("destino","").strip() # ← AHORA EN BLANCO
        patente = request.POST.get("patente","").strip()
        chofer = request.POST.get("chofer","").strip()
        
        # Validar que ingrese datos reales
        if not origen or not destino:
            return render(request, "viajes/iniciar.html", {"error": "Debes ingresar origen y destino"})
        
        # Generar código LASAMA-RENG-CHIL-YYYYMMDD-001
        from datetime import datetime
        hoy = datetime.now().strftime("%Y%m%d")
        count = Viaje.objects.filter(codigo__contains=hoy).count() + 1
        codigo = f"LASAMA-{origen[:4].upper()}-{destino[:4].upper()}-{hoy}-{count:03d}"

        viaje = Viaje.objects.create(
            codigo=codigo,
            origen=origen,
            destino=destino,
            patente=patente,
            chofer=chofer
        )
        return redirect(f"/viaje/{codigo}/")
    return render(request, "viajes/iniciar.html")
def detalle_viaje(request, codigo):
    viaje = get_object_or_404(Viaje, codigo=codigo)
    peajes = viaje.peajes.all()
    total = peajes.aggregate(Sum('monto'))['monto__sum'] or 0
    return render(request, 'viajes/detalle.html', {'viaje': viaje, 'peajes': peajes, 'total': total})

def agregar_peaje(request, codigo):
    viaje = get_object_or_404(Viaje, codigo=codigo)
    if request.method == 'POST':
        Peaje.objects.create(
            viaje=viaje,
            plaza=request.POST.get('plaza'),
            monto=request.POST.get('monto') or 0,
            tipo=request.POST.get('tipo','TRONCAL'),
            foto=request.FILES.get('foto'),
        )
        return redirect('detalle_viaje', codigo=codigo)
    return render(request, 'viajes/agregar.html', {'viaje': viaje})

def finalizar_viaje(request, codigo):
    viaje = get_object_or_404(Viaje, codigo=codigo)
    viaje.finalizado = True
    viaje.fecha_fin = timezone.now()
    viaje.save()
    # Aquí va tu envío de email a finanzas@lasama.cl con Excel/PDF (ya lo tenías)
    return render(request, 'viajes/finalizado.html', {'viaje': viaje})
