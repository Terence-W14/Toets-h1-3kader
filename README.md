# Klas 3 Hoofdstuk 1 – Hoe welvarend ben jij? (Versie A)

**Nieuwe, afzonderlijke website** voor 3 vmbo-k. 17 vragen, 21 punten.

## Render installeren
1. Maak een **nieuwe GitHub-repository**; upload de inhoud van deze ZIP (niet de ZIP zelf).
2. Maak een **nieuwe Neon-database**. Gebruik NOOIT de DATABASE_URL van de bestaande hoofdstuk-2-website: de tabelnamen zijn gelijk.
3. Maak een nieuwe Render Web Service gekoppeld aan de nieuwe repository.
4. Build: `pip install -r requirements.txt`; start: `gunicorn --workers 2 --bind 0.0.0.0:$PORT app:app`.
5. Zet environment variables: `DATABASE_URL` (nieuwe Neon PostgreSQL), `SECRET_KEY` (lange willekeurige waarde), `TEACHER_PASSWORD_HASH` (werkzeug scrypt/pbkdf2 hash). Deel wachtwoorden niet in de chat.
6. Open `/docent/login`, controleer knoppen openen/sluiten en PDF, test met een fictieve leerling.

## Functies
- Toets standaard gesloten; docent opent/sluit via `/docent`.
- Autosave antwoorden; automatische beoordeling bij 1, 6, 8, 11, 12, 16.
- Handmatige beoordeling van overige vragen in één keer opslaan per leerling.
- Ingeleverde en vergrendelde toetsen nakijken; PDF per leerling; CSV/JSON-backups.
- Cijfer = 1 + 9 × (punten / 21).

## Let op
De toetsvergrendeling bij tabblad verlaten is afhankelijk van de browser. Browser sluiten of netwerkverlies is niet altijd detecteerbaar. Niet-ingeleverde, niet-vergrendelde toetsen kunnen door de docent op de leerlingpagina handmatig als verlaten worden gemarkeerd. Doe dit alleen als de leerling echt gestopt is.

De taartgrafiek bij vraag 4 is een nieuwe, vereenvoudigde weergave met dezelfde percentages (27/32/28/13) als de bron.
