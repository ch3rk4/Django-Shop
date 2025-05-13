from django.shortcuts import render


def home_view(request):
    """
    Контроллер для отображения домашней страницы.
    """
    return render(request, 'catalog/home.html')


def contacts_view(request):
    """
    Контроллер для отображения и обработки страницы контактов.
    """
    success_message = None

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        success_message = 'Ваше сообщение успешно отправлено!'

    context = {
        'success_message': success_message
    }

    return render(request, 'catalog/contacts.html', context)