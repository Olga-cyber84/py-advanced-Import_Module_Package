import animalapi as a


def get_animal():
    data = a.rand_animals()
    img = data["image"]
    fact = data["fact"]
    print(fact)


if __name__ == '__main__':
    get_animal()
