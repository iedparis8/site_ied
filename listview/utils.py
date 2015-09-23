import requests


def get_personnel():
    url = 'https://backoffice.iedparis8.net/personnel/personnels'
    return requests.get(url).json()


def get_personnel_member(id):
    url = 'https://backoffice.iedparis8.net/personnel/personnels/' + str(id)
    return requests.get(url).json()
