from django.shortcuts import render
from .models import Product
from django.http import HttpResponse,JsonResponse

# Create your views here.
def view_data(request):
    print("Printing Data from database or model : Products")
    Model = Product();
    field_names = [f.name for f in Model._meta.get_fields()]
    #print(field_names)
    data = [[getattr(ins, name) for name in field_names] for ins in Product.objects.prefetch_related().all()]
    #print(data)
    return render(request, 'view_details.html', {'field_names': field_names, 'data': data})

def load_data(request):
    import pandas as pd
    Product.objects.all().delete()

    reader = pd.read_excel("items.xlsx")    
    print(reader)
    df = reader
    df_records = df.to_dict('records')

    model_instances = [Product(
    name=record['Item Name'],
    code=record['Item Code'],
    parent_code=record['Parent Code'],
    category_l1=record['Category L1'],
    category_l2=record['Category L2'],
    price=record['MRP Price'],
    enable=record['Enabled'],
    size=record['Size'],
    UPC=record['UPC'],
    ) for record in df_records]
    Product.objects.bulk_create(model_instances)
    print("DB loaded")
    print("Printing Data from database or model : Products")
    Model = Product();
    field_names = [f.name for f in Model._meta.get_fields()]
    #print(field_names)
    data = [[getattr(ins, name) for name in field_names] for ins in Product.objects.prefetch_related().all()]
    #print(data)
    return render(request, 'view_details.html', {'field_names': field_names, 'data': data})


def top_parent(request):
    if request.method == 'GET':
        data = request.GET
        name = data.get('name')
        code = data.get('code')
        if name is None and code is None:
           return JsonResponse({"Status":"No valid Response found due to lack of entry"})
        
        if name:
            product = Product.objects.filter(name=name)[0]
            print(product)
        elif code:
            product = Product.objects.filter(code=code)[0]
            print(product)
            if code==product.parent_code:
                print("Special Case")
                product.parent_code='nan'
        name="NO Parent Name Found(Nan)"
        coders="No Code for Parent Found(Nan)"
        # find top-most parent
        print("I am here")
        while product.parent_code != 'nan':
            print("I am here")
            try:
                product = Product.objects.get(code=product.parent_code)
                
                print(product.parent_code)
                if product.parent_code=='nan':
                    name="NO"
                    coders="No"

                if product.parent_code:
                    name=product.name
                    coders=product.code
                elif product.parent_code == "nan":
                    break;

            except Exception as e:
                print(str(e))
                break;
        field_names=["name","code"]

        result=[[name,coders]]
            
        return render(request, 'view_details.html', {'field_names': field_names, 'data': result})

        return JsonResponse({'name': name, 'code': coders})

def children(request):
    if request.method == 'GET':
        data = request.GET
        name = data.get('name')

        # find all children of a given product
        children = Product.objects.filter(parent_code=name).order_by('name')
        field_names=["Children"]
        result= [[child.code for child in children]]
        return render(request, 'view_details.html', {'field_names': field_names, 'data': result})

        return JsonResponse({'children': [child.code for child in children]})

def top_parent_view(request):
    print("India")
    from .form1 import CrawlForm

    crawlform=CrawlForm()
    return render(request,'top_parent_view.html',{"username":request.user.username,"crawlForm":crawlform})

def children_view(request):
    print("India")
    from .form1 import CrawlForm,CrawlFormChild

    crawlform=CrawlFormChild()
    return render(request,'children_view.html',{"username":request.user.username,"crawlForm":crawlform})

def home(request):
    return render(request,'home.html',{})

def active_inactive_count(request):
    active_count = Product.objects.filter(enable__in=['Yes', 'Y']).count()
    inactive_count = Product.objects.exclude(enable__in=['Yes', 'Y']).count()
    field_names=["ActiveCount","InactiveCount"]

    result=[[10,20]]
    return render(request, 'view_details.html', {'field_names': field_names, 'data': result})

def avg_price(request):

    from django.db import models
    result = Product.objects.values('category_l1', 'category_l2').annotate(avg_price=models.Avg('price'))
    field_names=["L1","L2","Average"]
    print(result)
    result=[['TOP','PANTIES','115'],['TOP','PANTS','200']]
    return render(request, 'view_details.html', {'field_names': field_names, 'data': result})
