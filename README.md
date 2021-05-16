# Ohjelmistotekniikka, kevät 2021

Tämä on Helsingin yliopiston ot-harjoitustyökurssissa kehitetty työpöytäsovellus, jonka avulla käyttäjät pystyvät laatimaan fyysiset harjoitussessiot ja näkemään raporttia suorituksista.

## Huomio Python-versiosta

Sovelluksen toiminta on testattu Python-versiolla 3.6.0. Etenkin vanhempien Python-versioiden kanssa saattaa ilmentyä ongelmia.

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](./dokumentaatio/käyttöohje.md)
- [Testaus](./dokumentaatio/testaus.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```

### Refaktorointi

Src-hakemistossa olevaa koodia voi refaktoroida komennolla:

```bash
poetry run invoke refactor
```
