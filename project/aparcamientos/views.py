import xml.etree.ElementTree as ET
from django.core import serializers
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Aparcamiento, AparcaSeleccionado, Comentario, Css
from django.contrib.auth import logout, login
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
import urllib

#from __future__ import unicode_literals
#import aparcamientos.feedparser as feedparser

def userLog(request):
    user = False
    if request.user.is_authenticated():
        respuesta = "Logged in as " + request.user.username + ". "
        respuesta += '<a href="/logout">Logout</a>'
    else:
        respuesta = "Not logged in. " + '<a href="/login">Login</a>'
    return respuesta

def usuariosLat(request):
    # Muestra los enlaces a páginas personales en columna lateral
    luser = []
    luserObj = AparcaSeleccionado.objects.all()
    for a in luserObj:
        add = a.usuario
        if add not in luser:
            luser.append(add)
        return luser

def parsear(request):
    #d = feedparser.parse('http://datos.munimadrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=202584-0-aparcamientos-residentes&mgmtid=e84276ac109d3410VgnVCM2000000c205a0aRCRD&preview=full')
    munimadrid = 'http://datos.munimadrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=202584-0-aparcamientos-residentes&mgmtid=e84276ac109d3410VgnVCM2000000c205a0aRCRD&preview=full'
    xml = urllib.request.urlopen(munimadrid)
    tree = ET.parse(xml)
    root = tree.getroot()
    #for child in root:
        #for grandson in child:
           #respuesta += grandson.tag + str(grandson.attrib)
    #grandson = root.findall('contenido')
    #respuesta += str(grandson)
    cont = 0
    lista = []
    #for neighbor in root.findall('atributos'):
    #     for texto in neighbor.itertext():
    #         lista = lista.append(texto)
    for neighbor in root.iter('atributos'):
        email,phone,num = "", "", ""
        for filaBD in neighbor.iterfind('atributo'):
            #dic = filaBD.attrib
            for elem in filaBD.attrib:
                if elem.find('atributo'):
                    for x in filaBD.iterfind('atributo'):
                        for varsDir in x.attrib:
                            if x.attrib[varsDir]=="CLASE-VIAL": # or "NUM":
                                via = ' '.join(x.itertext())
                            elif x.attrib[varsDir]== "NOMBRE-VIA":
                                street = ' '.join(x.itertext())
                            elif x.attrib[varsDir]== "NUM":
                                num = ' '.join(x.itertext())
                            elif x.attrib[varsDir]== "CODIGO-POSTAL":
                                postal = ' '.join(x.itertext())
                            elif x.attrib[varsDir]== "LOCALIDAD":
                                city = ' '.join(x.itertext())
                            elif x.attrib[varsDir]=="LATITUD":
                                lat=' '.join(x.itertext())
                            elif x.attrib[varsDir]=="LONGITUD":
                                l = ' '.join(x.itertext())
                            elif x.attrib[varsDir]=="BARRIO":
                                bar = ' '.join(x.itertext())
                            elif x.attrib[varsDir]=="DISTRITO":
                                district = ' '.join(x.itertext())
                            elif x.attrib[varsDir]=="TELEFONO":
                                phone = ' '.join(x.itertext())
                            elif x.attrib[varsDir]=="EMAIL":
                                email = ' '.join(x.itertext())
                if filaBD.attrib[elem]=="NOMBRE":
                    name = ' '.join(filaBD.itertext())
                elif filaBD.attrib[elem]=="CONTENT-URL":
                    url = ' '.join(filaBD.itertext())
                elif filaBD.attrib[elem]=="ACCESIBILIDAD":
                    access = int(' '.join(filaBD.itertext()))
                elif filaBD.attrib[elem]=="DESCRIPCION":
                    descrip = ' '.join(filaBD.itertext())
                elif filaBD.attrib[elem]=="LOCALIZACION":
                    address2 = ' '.join(filaBD.itertext())
        address = " ".join([via, street, num, postal, city]) # + city
        contenido = Aparcamiento(id=cont,nombre=name,url=url,dir2=address,latitud=lat,longitud=l,descripcion=descrip,accesible=access,barrio=bar,distrito=district,email=email,telf=phone)
        contenido.save()
        cont = cont +1
    lAparcaParseada = Aparcamiento.objects.all()
    return lAparcaParseada

@csrf_exempt
def mostrar_todo(request):
    maxListar = 5
    validar,acceso = 0, 0
    cruz = 'unchecked'
    luser = []
    user = request.user.username
    regUsuarios = userLog(request)
    lAparcamientos = Aparcamiento.objects.all().order_by("-ncomment")[:5]
    titulo = " Los aparcamientos almacenados son:"
    if request.method == 'POST':
        acceso=request.POST.get('Accesible')
        if request.user.is_authenticated():
            user = request.user.username
            if '_submit' in request.POST:
                validar = 1
            if validar or not len(lAparcamientos):
                lAparcamientos = parsear(request)
                lAparcamientos = Aparcamiento.objects.all().order_by("-ncomment")[:5]
    #ko = Aparcamiento.objects.get(ncomment=0) #get
    #ko.delete()
    #Filtrar por numero de comentarios
    #lAparcaOrden = Aparcamiento.objects.all().order_by("-ncomment")[0:10]
    num = int(lAparcamientos[0].ncomment)
    print(num)
    #for aparca in lAparcaOrden:
    #num = str(1):
    #lAparcamientos = Aparcamiento.objects.filter(ncomment=num)
        #num = num - 1
    if acceso:
        lAparcamientos = Aparcamiento.objects.filter(accesible=acceso)
        cruz = 'checked'
    # Muestra los enlaces a páginas personales en columna lateral
    luserObj = AparcaSeleccionado.objects.all()
    for a in luserObj:
        add = a.usuario
        if add not in luser:
            luser.append(add)
    plantilla = get_template("businessxhtml/index.html")
    c = Context({'name': titulo, 'listaAparca': lAparcamientos, 'users': luser, 'login': regUsuarios, 'acceso':cruz, 'usuario': user})
    return HttpResponse(plantilla.render(c))

@csrf_exempt
def aparcamientos(request):
    filtro = "None"
    lDistritos = []
    lusers = usuariosLat(request)
    regUsuarios = userLog(request)
    respuesta = "Todos los aparcamientos son:"
    lAparcamientos = Aparcamiento.objects.all()
    #lDistr = Aparcamiento.objects.annotate(distrito)
    #lDistritos = Aparcamiento.objects.update("distrito")
    for a in lAparcamientos:
        add = a.distrito
        if add not in lDistritos:
            lDistritos.append(add)
    if request.method == 'POST':
        filtro = request.POST.get('filtro')
        if filtro != "None":
            dis = request.POST['distrito']
            if dis in lDistritos:
                lAparcamientos = Aparcamiento.objects.filter(distrito=dis)
        else:
            lAparcamientos = Aparcamiento.objects.all()
        if request.user.is_authenticated():
            user = request.user.username
            if '_submit' in request.POST:
                cuerpo = request.body.decode('utf-8')
                ap_id = int(cuerpo.split('=')[-1])
                lApSel = AparcaSeleccionado.objects.all() #.order_by("-ncomment")
                ko = AparcaSeleccionado.objects.filter(aparcamiento=ap_id)
                if not len(ko):
                    #respuesta += "Aparcamiento no almacenado"
                    info = Aparcamiento.objects.get(id=ap_id)
                    addAp = AparcaSeleccionado(usuario=user, aparcamiento=info)
                    addAp.save()
                else:
                    print(ko)
    plantilla = get_template("businessxhtml/aparcamientos.html")
    c = Context({'listaAparca': lAparcamientos, 'content':respuesta, 'login': regUsuarios, 'users': lusers, 'listadistrito':lDistritos})
    return HttpResponse(plantilla.render(c))

@csrf_exempt
def aparca_id(request, ap_id):
    regUsuarios = userLog(request)
    lusers = usuariosLat(request)
    ap_id = int(ap_id.split('/')[-1])
    respuesta = "Página de aparcamiento seleccionado"
    if request.method == 'GET':
        try:
            info = Aparcamiento.objects.get(id=ap_id)
            comentario = Comentario.objects.filter(aparcamiento=ap_id)
        except Aparcamiento.DoesNotExist:
            respuesta += "Aparcamiento no almacenado"
        except Comentario.DoesNotExist:
            respuesta += "No tiene comentarios."
    elif request.method == 'POST':
        if request.user.is_authenticated():
            com = request.POST['comment']
            info = Aparcamiento.objects.get(id=ap_id)
            addcom = Comentario(contenido=com, aparcamiento=info)
            addcom.save()
            info.ncomment += 1

    enlace = request.get_host()
    comentario = Comentario.objects.filter(aparcamiento=ap_id)
    plantilla = get_template("businessxhtml/aparcamiento.html")
    c = Context({'aparca': info, 'content':respuesta,'login':regUsuarios, 'dir': enlace, 'users': lusers, 'lcomment':comentario})
    return HttpResponse(plantilla.render(c))
    # usermame lista de usuarios login redirige a la principal filter distrito title??? accesible get_path en plantillas....respuesta

@csrf_exempt
def usuario(request, recurso):
    regUsuarios = userLog(request)
    lusers = usuariosLat(request)
    cuerpo = request.body
    user = recurso.split('/')[0]
    #user = request.user.username
    respuesta = "Página de usuario"
    if request.method == 'GET':
        try:
            lAparcaUser = AparcaSeleccionado.objects.filter(usuario=recurso)[:5]
        except AparcaSeleccionado.DoesNotExist:
            respuesta += recurso + " no tiene aparcamientos seleccionados"

    elif request.method == 'POST':
        lAparcaUser = AparcaSeleccionado.objects.filter(usuario=recurso)[:5]
        if request.user.is_authenticated():
            user = request.user.username
            background = request.POST['fondo']
            size = request.POST['letraTam']
            title = request.POST['titulo']
            try:
                cssObj = Css.objects.get(usuario=user)
                if user == cssObj.usuario:
                    cssObj = Css.objects.get(id=cssObj.id)
                    cssObj.tamLetra=size
                    cssObj.colorFondo=background
                    cssObj.titulo=title
                    #contenido = cssObj(tamLetra=size, colorFondo=background, titulo=title)
                cssObj.save()
            except:
                t= "Pagina de " + user
                #cssObj = Css.objects.get(usuario=user)
                contenido = Css(usuario=user, tamLetra=size, colorFondo=background ,titulo=t)
                contenido.save()
            if '_submit' in request.POST:
                cuerpo = request.body.decode('utf-8')
                ap_id = int(cuerpo.split('=')[-1])
                #lApSel = AparcaSeleccionado.objects.all() #.order_by("-ncomment")
                ko = AparcaSeleccionado.objects.get(aparcamiento=ap_id) #get
                ko.delete()
        if len(lAparcaUser) > 5:
            lAparcaUser = AparcaSeleccionado.objects.filter(usuario=recurso)[5:10]
    plantilla = get_template("businessxhtml/usuario.html")
    c = Context({'listaAparca': lAparcaUser, 'content':respuesta, 'login': regUsuarios, 'users': lusers, 'usuario':user})
    return HttpResponse(plantilla.render(c))

def user_xml(request, recurso):
    user = recurso.split('/')[0]
    lAparcaUser = AparcaSeleccionado.objects.filter(usuario=user)
    hijos = serializers.serialize("xml" ,lAparcaUser)
    f = open('usuario.xml',"w")
    f.write(hijos)
    f.close()
    f2 = open('usuario.xml',"r")
    xml = f2.read()
    return HttpResponse(xml, content_type='text/xml')

@csrf_exempt
def css(request):
    if request.user.is_authenticated():
        user = request.user.username
        css = Css.objects.get(usuario=user)
    plantilla = get_template("businessxhtml/style.css")
    c = Context({'varsCss': css.colorFondo })
    redirect('/style.css')
    return HttpResponse(plantilla.render(c), content_type="text/css")
