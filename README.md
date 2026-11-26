
# Testfallsregister

Ett enkelt testfallsregister utvecklat i Python.

## Om systemet

Syftet med systemet är att hjälpa en testgrupp att registrera och hålla ordning på sina testfall.

### Funktioner

Användaren kan:
- Registrera nya testfall
- Visa alla registrerade testfall
- Avsluta programmet

Varje testfall innehåller:
- **Titel**
- **Beskrivning**
- **Förväntat resultat**

### Begränsningar

- Testfallen sparas endast medan programmet körs.
- Informationen försvinner när programmet avslutas.
- Programmet genomför inte några tester.


## Programmets uppbyggnad

| `main.py` | Innehåller programmets meny och huvudlogik. |
| `test_case.py` | Innehåller klassen `TestCase`. |
| `test_case_repository.py` | Innehåller klassen `TestCaseRepository`. |


## Starta programmet

1. Öppna projektmappen i Visual Studio Code.
2. Öppna terminalen.
3. Kör kommandot:


