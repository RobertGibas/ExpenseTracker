from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ExpenseForm, ExpenseFilterForm
from .models import Expense


@login_required
def expense_list(request: HttpRequest) -> HttpResponse:
    qs = Expense.objects.filter(user=request.user).select_related("category")

    filter_form = ExpenseFilterForm(request.GET or None)
    if filter_form.is_valid():
        start = filter_form.cleaned_data.get("start_date")
        end = filter_form.cleaned_data.get("end_date")
        category = filter_form.cleaned_data.get("category")
        if start:
            qs = qs.filter(date__gte=start)
        if end:
            qs = qs.filter(date__lte=end)
        if category:
            qs = qs.filter(category=category)

    total_sum = qs.aggregate(total=Sum("amount"))["total"] or 0
    paginator = Paginator(qs, 20)
    page = request.GET.get("page")
    expenses = paginator.get_page(page)

    return render(
        request,
        "expenses/expense_list.html",
        {"expenses": expenses, "filter_form": filter_form, "total_sum": total_sum},
    )


@login_required
def expense_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect("expenses:list")
    else:
        form = ExpenseForm()
    return render(request, "expenses/expense_form.html", {"form": form})


@login_required
def expense_update(request: HttpRequest, pk: int) -> HttpResponse:
    expense = get_object_or_404(Expense, pk=pk)
    if expense.user != request.user:
        return HttpResponseForbidden("Brak dostępu.")
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("expenses:list")
    else:
        form = ExpenseForm(instance=expense)
    return render(request, "expenses/expense_form.html", {"form": form})


@login_required
def expense_delete(request: HttpRequest, pk: int) -> HttpResponse:
    expense = get_object_or_404(Expense, pk=pk)
    if expense.user != request.user:
        return HttpResponseForbidden("Brak dostępu.")
    if request.method == "POST":
        expense.delete()
        return redirect("expenses:list")
    return render(request, "expenses/expense_confirm_delete.html", {"expense": expense})


@login_required
def expense_summary(request: HttpRequest) -> HttpResponse:
    qs = Expense.objects.filter(user=request.user).select_related("category")
    filter_form = ExpenseFilterForm(request.GET or None)
    if filter_form.is_valid():
        start = filter_form.cleaned_data.get("start_date")
        end = filter_form.cleaned_data.get("end_date")
        category = filter_form.cleaned_data.get("category")
        if start:
            qs = qs.filter(date__gte=start)
        if end:
            qs = qs.filter(date__lte=end)
        if category:
            qs = qs.filter(category=category)

    by_category = (
        qs.values("category__name")
        .annotate(total=Sum("amount"))
        .order_by("-total")
    )
    total_sum = qs.aggregate(total=Sum("amount"))["total"] or 0

    return render(
        request,
        "expenses/summary.html",
        {"filter_form": filter_form, "by_category": by_category, "total_sum": total_sum},
    )