import csv
import os
from films_data import films_data
from genres import genres_data

# Створення директорій та запис у CSV-файли для кожного жанру
for genre_name in genres_data:
    directory_name = f"./{genre_name}"

    # Перевірка наявності директорії перед створенням
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    # Створення та запис у CSV-файли для кожного жанру
    for film_data in films_data:
        for genre_data in film_data['gen']:
            if genre_data['genre'] == genre_name:
                csv_file_path = os.path.join(directory_name, f"{genre_name}_movies.csv")
                file_exists = os.path.exists(csv_file_path)

                with open(csv_file_path, 'a', newline='', encoding='utf-8') as csvfile:
                    fieldnames = ['title', 'year', 'rating', 'type', 'genres']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    # Запис заголовків колонок, якщо файл тільки що створений
                    if not file_exists:
                        writer.writeheader()

                    # Запис інформації про фільм у CSV-файл
                    writer.writerow({
                        'title': film_data['title'],
                        'year': film_data['year'],
                        'rating': film_data['rating'],
                        'type': film_data['type'],
                        'genres': ";".join(genre['genre'] for genre in film_data['gen'])
                    })

print("CSV-файли для кожного жанру були створені та заповнені інформацією про фільми.")
