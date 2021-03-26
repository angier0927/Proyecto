from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render

def firtsView(request):

    return HttpResponse("Hola Mundo")


def index(request, agno, actual):

    edad = actual - agno

    #read_template = open("C:/Users/3mer/Documents/Projects/P3UR/blog/blog/blog/template/index.html")

    #plt = Template(read_template.read())

    #read_template.close()

    doc_ext = loader.get_template('index.html')

    #ctx = Context({"nn": edad, "asignaturas": ['BSI', 'L P3', 'BD1', 'ASRI']})

    ctx = {"nn": edad, "asignaturas": ['BSI', 'L P3', 'BD1', 'ASRI']}

    doc = doc_ext.render(ctx)

    return HttpResponse(doc)


def index2(request):

    ctx = {"nn": 25, "asignaturas": ['BSI', 'L P3', 'BD1', 'ASRI']}

    return render(request, "index.html", ctx)
