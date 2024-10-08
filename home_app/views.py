from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .forms import ClientForm, ProductForm
from .models import Client, Product, Order


def index(request):
    return render(request, 'index.html')


# Представление для создания клиента
def create_client_view(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_clients')
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})


# Представление для отображения всех клиентов
def all_clients_view(request):
    clients = Client.objects.all()
    return render(request, 'all_clients.html', {'clients': clients})


# Представление для обновления клиента
def update_client_view(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('all_clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'update_client.html', {'form': form, 'client': client})


# Представление для удаления клиента
def delete_client_view(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('all_clients')
    return render(request, 'delete_client.html', {'client': client})


def client_ordered_products(request, client_id, days):
    # Определите дату, за которую вы хотите получить заказы
    end_date = timezone.now()
    start_date = end_date - timezone.timedelta(days=days)

    # Получите все заказы клиента за выбранный период времени
    orders = Order.objects.filter(client_id=client_id, order_date__range=(start_date, end_date))

    # Получите список товаров из всех заказов клиента
    ordered_products = []
    for order in orders:
        ordered_products.extend(order.products.all())

    # Удалите повторяющиеся товары из списка
    unique_ordered_products = list(set(ordered_products))

    # Отсортируйте товары по времени заказа
    sorted_ordered_products = sorted(unique_ordered_products, key=lambda x: x.order.order_date, reverse=True)

    context = {
        'client_id': client_id,
        'ordered_products': sorted_ordered_products,
        'days': days,
    }
    return render(request, 'client_ordered_products.html', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})


def update_product_view(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form, 'product': product})


def delete_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'confirm_delete_product.html', {'product': product})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def client_orders(request, client_id):
    client = Client.objects.get(pk=client_id)

    # За последние 7 дней
    last_7_days = timezone.now() - timedelta(days=7)
    client_orders_last_7_days = Product.objects.filter(order__client=client, order__order_date__gte=last_7_days).distinct()

    # За последние 30 дней
    last_30_days = timezone.now() - timedelta(days=30)
    client_orders_last_30_days = Product.objects.filter(order__client=client, order__order_date__gte=last_30_days).distinct()

    # За последние 365 дней
    last_365_days = timezone.now() - timedelta(days=365)
    client_orders_last_365_days = Product.objects.filter(order__client=client, order__order_date__gte=last_365_days).distinct()

    return render(request, 'home_app/client_orders.html', {
        'client_orders_last_7_days': client_orders_last_7_days,
        'client_orders_last_30_days': client_orders_last_30_days,
        'client_orders_last_365_days': client_orders_last_365_days,
    })