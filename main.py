import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

wishes = [
    {
        "name": "Vœu 1",
        "data": [
            {"y": 87, "name": "Recherche"},
            {"y": 33, "name": "Innovation et intrapreneuriat "},
            {"y": 35, "name": "Conception de systèmes complexes"},
            {"y": 64, "name": "Management de projet et transformation"},
            {"y": 40, "name": "Management opérationnel "},
            {"y": 152, "name": "Métiers d'analyse et d'aide à la décision"},
            {"y": 11, "name": "Commercial et développement d'affaires "},
            {"y": 26, "name": "CentraleSupelec Entrepreneur"},
        ],
    },
    {
        "name": "Vœu 2",
        "data": [
            {"y": 27, "name": "Recherche"},
            {"y": 67, "name": "Innovation et intrapreneuriat "},
            {"y": 69, "name": "Conception de systèmes complexes"},
            {"y": 108, "name": "Management de projet et transformation"},
            {"y": 69, "name": "Management opérationnel "},
            {"y": 62, "name": "Métiers d'analyse et d'aide à la décision"},
            {"y": 29, "name": "Commercial et développement d'affaires "},
            {"y": 17, "name": "CentraleSupelec Entrepreneur"},
        ],
    },
    {
        "name": "Vœu 3",
        "data": [
            {"y": 23, "name": "Recherche"},
            {"y": 69, "name": "Innovation et intrapreneuriat "},
            {"y": 64, "name": "Conception de systèmes complexes"},
            {"y": 83, "name": "Management de projet et transformation"},
            {"y": 85, "name": "Management opérationnel "},
            {"y": 57, "name": "Métiers d'analyse et d'aide à la décision"},
            {"y": 43, "name": "Commercial et développement d'affaires "},
            {"y": 24, "name": "CentraleSupelec Entrepreneur"},
        ],
    },
    {
        "name": "Vœu 4",
        "data": [
            {"y": 23, "name": "Recherche"},
            {"y": 62, "name": "Innovation et intrapreneuriat "},
            {"y": 60, "name": "Conception de systèmes complexes"},
            {"y": 85, "name": "Management de projet et transformation"},
            {"y": 75, "name": "Management opérationnel "},
            {"y": 53, "name": "Métiers d'analyse et d'aide à la décision"},
            {"y": 64, "name": "Commercial et développement d'affaires "},
            {"y": 26, "name": "CentraleSupelec Entrepreneur"},
        ],
    },
    {
        "name": "Vœu 5",
        "data": [
            {"y": 33, "name": "Recherche"},
            {"y": 77, "name": "Innovation et intrapreneuriat "},
            {"y": 63, "name": "Conception de systèmes complexes"},
            {"y": 60, "name": "Management de projet et transformation"},
            {"y": 67, "name": "Management opérationnel "},
            {"y": 41, "name": "Métiers d'analyse et d'aide à la décision"},
            {"y": 63, "name": "Commercial et développement d'affaires "},
            {"y": 44, "name": "CentraleSupelec Entrepreneur"},
        ],
    },
    {
        "name": "Vœu 6",
        "data": [
            {"y": 52, "name": "Recherche"},
            {"y": 79, "name": "Innovation et intrapreneuriat "},
            {"y": 61, "name": "Conception de systèmes complexes"},
            {"y": 31, "name": "Management de projet et transformation"},
            {"y": 67, "name": "Management opérationnel "},
            {"y": 49, "name": "Métiers d'analyse et d'aide à la décision"},
            {"y": 56, "name": "Commercial et développement d'affaires "},
            {"y": 53, "name": "CentraleSupelec Entrepreneur"},
        ],
    },
    {
        "name": "Vœu 7",
        "data": [
            {"y": 72, "name": "Recherche"},
            {"y": 44, "name": "Innovation et intrapreneuriat "},
            {"y": 68, "name": "Conception de systèmes complexes"},
            {"y": 13, "name": "Management de projet et transformation"},
            {"y": 29, "name": "Management opérationnel "},
            {"y": 27, "name": "Métiers d'analyse et d'aide à la décision"},
            {"y": 124, "name": "Commercial et développement d'affaires "},
            {"y": 71, "name": "CentraleSupelec Entrepreneur"},
        ],
    },
    {
        "name": "Vœu 8",
        "data": [
            {"y": 131, "name": "Recherche"},
            {"y": 17, "name": "Innovation et intrapreneuriat "},
            {"y": 28, "name": "Conception de systèmes complexes"},
            {"y": 4, "name": "Management de projet et transformation"},
            {"y": 16, "name": "Management opérationnel "},
            {"y": 7, "name": "Métiers d'analyse et d'aide à la décision"},
            {"y": 58, "name": "Commercial et développement d'affaires "},
            {"y": 187, "name": "CentraleSupelec Entrepreneur"},
        ],
    },
]

sectors = {
    "Recherche": 100,
    "Innovation et intrapreneuriat ": 80,
    "Conception de systèmes complexes": 80,
    "Management de projet et transformation": 100,
    "Management opérationnel ": 100,
    "Métiers d'analyse et d'aide à la décision": 110,
    "Commercial et développement d'affaires ": 50,
    "CentraleSupelec Entrepreneur": 70,
}


def reformat_wishes(wishes: list):
    """Reformat of the original wishes dictionnary"""
    reformatted_wishes = dict()
    for wish in wishes:
        wish_name = wish["name"]
        sectors = wish["data"]
        for sector in sectors:
            sector_name = sector["name"]
            wishes_number = sector["y"]

    return reformatted_wishes


def voters_number(wishes: list):
    """Returns the number of participants to the survey"""
    sectors = wishes[0]["data"]
    voters_number = 0
    for sector in sectors:
        voters_number += sector["y"]
    return voters_number


def get_total_places_number(sectors: dict):
    total_places_number = 0
    for key, val in sectors.items():
        total_places_number += val
    return total_places_number


def get_reformatted_first_wish_stats(wishes: list):
    first_wishes_stats = wishes[0]["data"]
    reformatted_first_wish_stats = dict()
    for sector_stats in first_wishes_stats:
        reformatted_first_wish_stats["{0}".format(sector_stats["name"])] = sector_stats[
            "y"
        ]
    return reformatted_first_wish_stats


voters_number = voters_number(wishes=wishes)
total_places_number = get_total_places_number(sectors=sectors)
reformatted_wishes = reformat_wishes(wishes=wishes)
reformatted_first_wish_stats = get_reformatted_first_wish_stats(wishes=wishes)

print("Number of voters :", voters_number)
print("Number of total places :", total_places_number)
print("Reformatted wishes :", reformatted_wishes)
print("Reformatted first wish stats", reformatted_first_wish_stats)


def plot_example_chart(sectors: dict, reformatted_first_wish_stats: dict):
    data = {
        "Nombre de places offertes": sectors.values(),
        "Nombre de voeu 1": reformatted_first_wish_stats.values(),
    }
    df = pd.DataFrame(
        data,
        index=list(sectors.keys()),
    )
    print(df)
    plt.style.use("ggplot")

    df.plot.barh()

    plt.title("Nombre de places offertes par filière")
    plt.ylabel("Filière")
    plt.show()


plot_example_chart(sectors, reformatted_first_wish_stats)
