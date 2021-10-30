from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from admins.forms import UserAdminsCreateForm, UserAdminsUpdateForm, ProductAdminsCreateForm
from products.models import Product
from users.models import User


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def admin_users_read(request):
    context = {
        'users': User.objects.all(),
    }
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminsCreateForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('admins:admin_users_read'))
        else:
            context = {
                'form': UserAdminsCreateForm()
            }

            return render(request, 'admins/admin-users-create.html', context)
    else:
        context = {
            'form': UserAdminsCreateForm()
        }

        return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, id):
    if request.method == 'POST':
        form = UserAdminsUpdateForm(data=request.POST, files=request.FILES, instance=User.objects.get(id=id))

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('admins:admin_users_read'))
        else:
            context = {
                'form': UserAdminsUpdateForm(instance=User.objects.get(id=id)),
                'user': User.objects.get(id=id)
            }

            return render(request, 'admins/admin-users-update-delete.html', context)
    else:
        context = {
            'form': UserAdminsUpdateForm(instance=User.objects.get(id=id)),
            'user': User.objects.get(id=id)
        }

        return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, id):
    User.objects.get(id=id).delete()

    return HttpResponseRedirect(reverse('admins:admin_users_read'))


@user_passes_test(lambda u: u.is_superuser)
def admin_users_deactivate(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()

    return HttpResponseRedirect(reverse('admins:admin_users_read'))


@user_passes_test(lambda u: u.is_superuser)
def admin_users_activate(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()

    return HttpResponseRedirect(reverse('admins:admin_users_read'))


@user_passes_test(lambda u: u.is_staff)
def admin_products_read(request):
    context = {
        'products': Product.objects.all(),
    }

    return render(request, 'admins/admin-products-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductAdminsCreateForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('admins:admin_users_read'))
        else:
            context = {
                'form': UserAdminsCreateForm()
            }

            return render(request, 'admins/admin-users-create.html', context)
    else:
        context = {
            'form': UserAdminsCreateForm()
        }

        return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, id):
    User.objects.get(id=id).delete()

    return HttpResponseRedirect(reverse('admins:admin_users_read'))


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, id):
    if request.method == 'POST':
        form = UserAdminsUpdateForm(data=request.POST, files=request.FILES, instance=User.objects.get(id=id))

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('admins:admin_users_read'))
        else:
            context = {
                'form': UserAdminsUpdateForm(instance=User.objects.get(id=id)),
                'user': User.objects.get(id=id)
            }

            return render(request, 'admins/admin-users-update-delete.html', context)
    else:
        context = {
            'form': UserAdminsUpdateForm(instance=User.objects.get(id=id)),
            'user': User.objects.get(id=id)
        }

        return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductAdminsCreateForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('admins:admin_products_read'))
        else:
            context = {
                'form': ProductAdminsCreateForm(),
                'erorrs': form.errors
            }

            return render(request, 'admins/admin-products-create.html', context)
    else:
        context = {
            'form': ProductAdminsCreateForm()
        }

        return render(request, 'admins/admin-products-create.html', context)
