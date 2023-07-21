import csv
import os
from films_data import films_data
from genres import genres_data

for genre_name in genres_data:
    directory_name = f"./{genre_name}"

    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    for film_data in films_data:
        if any(genre["genre"] == genre_name for genre in film_data["gen"]):
            csv_file_path = os.path.join(directory_name, f"{genre_name}_movies.csv")
            file_exists = os.path.exists(csv_file_path)

            with open(csv_file_path, "a", newline="", encoding="utf-8") as csvfile:
                fieldnames = ["title", "year", "rating", "type", "genres"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                if not file_exists:
                    writer.writeheader()

                writer.writerow(
                    {
                        "title": film_data["title"],
                        "year": film_data["year"],
                        "rating": film_data["rating"],
                        "type": film_data["type"],
                        "genres": genre_name,
                    }
                )

print("CSV-файли для кожного жанру були створені та заповнені інформацією про фільми.")
