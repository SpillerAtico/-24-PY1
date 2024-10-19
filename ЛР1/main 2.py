# TODO Найдите количество книг, которое можно разместить на дискете


def BiblioDisk():
    full_memory = 1.44 * 1024 * 1024
    book_memory = 100 * 50 * 25 * 4

    answer = int(full_memory / book_memory)
    return answer

print(f"Количество книг, помещающихся на дискету: {BiblioDisk()}")


