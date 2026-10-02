from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Product, Review, Brand
from .forms import ReviewForm

def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        "catalog/product_list.html",
        {
            "products": products
        }
    )


def brand_list(request):
    brands = Brand.objects.all().order_by("name")

    return render(
        request,
        "catalog/brand_list.html",
        {
            "brands": brands
        }
    )


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    reviews = product.reviews.all().order_by("-created_at")

    if request.method == "POST":

        if not request.user.is_authenticated:
            return redirect("login")

        form = ReviewForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)

            review.product = product
            review.user = request.user

            review.save()

            return redirect("product_detail", pk=product.pk)

    else:
        form = ReviewForm()

    return render(
        request,
        "catalog/product_detail.html",
        {
            "product": product,
            "reviews": reviews,
            "form": form,
        }
    )

@login_required
def review_edit(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if review.user != request.user:
        return redirect("product_detail", pk=review.product.pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            form.save()
            return redirect("product_detail", pk=review.product.pk)

    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        "catalog/review_edit.html",
        {
            "form": form,
            "review": review,
        }
    )


@login_required
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if review.user != request.user:
        return redirect("product_detail", pk=review.product.pk)

    if request.method == "POST":
        product_pk = review.product.pk
        review.delete()

        return redirect("product_detail", pk=product_pk)

    return render(
        request,
        "catalog/review_delete.html",
        {
            "review": review,
        }
    )