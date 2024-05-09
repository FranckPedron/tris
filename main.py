import random


def generate_random_list(size, min, max):
    random_list = []
    for i in range(size):
        el = random.randint(min, max)
        random_list.append(el)
    return random_list


def selection_sort(tab):
    for unsorted_index in range(0, len(tab) - 1):
        min = tab[unsorted_index]
        min_index = unsorted_index
        for i in range(unsorted_index, len(tab)):
            if tab[i] < min:
                min = tab[i]
                min_index = i
        tab[min_index] = tab[unsorted_index]
        tab[unsorted_index] = min


random_tab = generate_random_list(100, -1000, 1000)
print("UNSORTED:", random_tab)
selection_sort(random_tab)
print("SORTED:  ", random_tab)
