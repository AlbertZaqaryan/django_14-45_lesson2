from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    result = 0
    if request.method == 'POST':
        n1 = int(request.POST.get('n1'))
        char = request.POST.get('char')
        n2 = int(request.POST.get('n2'))
        if char == '+':
            result = n1 + n2
        elif char == '-':
            result = n1 - n2
        elif char == '*':
            result = n1 * n2
        elif char == '/':
            try:
                result = n1 / n2
            except ZeroDivisionError:
                result = "Zero Error"
    return render(request, 'home.html', context={
        'res':result
    })

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        question = request.POST.get('question')
        with open('db.txt', 'a') as file:
            file.write(f'{email} --- {phone} --- {question}\n')
    return render(request, 'contact.html')


def admin(request):
    with open('db.txt', 'r') as file:
        res = file.read()
    res = res.split('\n')
    return render(request, 'admin.html', context={
        'info_list':res[:-1]
    })

def delete_user(request):
    name = request.GET.get('name')
    with open('db.txt', 'r') as file:
        res = file.read()
    res = res.split('\n')
    res.remove(name)
    with open('db.txt', 'w') as file:
        for i in res:
            file.write(f'{i}\n')
    return redirect('admin_page')