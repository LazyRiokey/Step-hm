from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def main_page(request):
    return HttpResponse("<h2>Главная страница</h2>")


def writers(request):
    writers_dict = {
        "Shakespeare": range(1594, 1614),
        "Hemingway": range(1917, 1961),
    }
    writers = request.GET.get("writers")
    year = request.GET.get("year")
    if writers != None:
        if writers in writers_dict and int(year) in writers_dict[writers]:
            return HttpResponse(
                f"<h2>Информация о книгах, которые написал {writers} за {year} год</h2>"
            )
        else:
            return HttpResponseRedirect(f"/writers/{writers}")
    else:
        return HttpResponse("<h2>Писатели</h2>")


def best_books(request):
    return HttpResponse("<h2>Топ лучших книг</h2>")


def check_writers(request, writer):
    writers_list = ["Hemingway", "Shakespeare"]
    if writer in writers_list:
        return HttpResponse(f"<h2>Страница с информацией о {writer}</h2>")
    else:
        return HttpResponseRedirect("/writers")


def check_book_id(request, book_id):
    if book_id <= 10:
        return HttpResponse(f"<h2>Книга №{book_id}</h2>")
    else:
        return HttpResponseRedirect("/books")


def writers_books(request, writer, w_book):
    w_books = {
        "Hemingway": [
            "The_Sun_Also_Rises",
            "A_Farewell_to_Arms",
            "To_Have_and_Have_Not",
            "For_Whom_the_Bell_Tolls",
            "Across_the_River_and_into_the_Trees",
            "The_Old_Man_and_the_Sea",
            "Islands_in_the_Stream",
            "The_Garden_of_Eden",
            "True_at_First_Light",
        ],
        "Shakespeare": [
            "A_Midsummer_Night’s_Dream",
            "Hamlet",
            "Romeo_and_Juliet",
            "Merchant_of_Venice",
            "Julius_Caesar",
            "Othello",
            "Macbeth",
        ],
    }

    if w_book in w_books[writer]:
        return HttpResponse(f"<h2>Информация о книге {w_book.replace('_', ' ')}</h2>")
    else:
        return HttpResponseRedirect(f"/writers/{writer}")
