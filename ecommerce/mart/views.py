from django.shortcuts import render
from django.http import HttpResponse
from django.utils.http import urlencode
# from django.views.generic import TemplateView

# function based view 
'''

class based view
class clasName(req):
    def post():
        pass
    def get():
        pass 

'''


def index(request):
    products = {"glasses": 550, "t-shirt": 700}
    if request.method == "POST":
        selected_items = request.POST.getlist("options")
        print(selected_items)
        base_url = "/show/"
        query_string = urlencode({"options": selected_items})
        url = f"{base_url}?{query_string}"
        return HttpResponse(url)

    return render(request, "mart/index.html", {"products_dict":products})

def show(request):
    selected_options = request.GET.getlist('options')
    render(request, "mart/show.html", {'products': selected_options})
    
    
# class cbv(TemplateView):
#     template_name = 'mart/cbv_test.html'
#     def get(self, request):
#         response = HttpResponse('hello')
#         return 
#     def post(self, request, ***args, **kwargs):
#         return 