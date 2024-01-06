
Dieses Programm generiert fake Daten, schickt sie zum Elastic Cloud und erfüllt spezifische Anforderungen, um explorativ Daten zu analysieren.

# Erklärung der Dateien

## 1. faker_firebase.ipynb
Dieses Program generiert fake Daten mittels Faker Modul und schickt sie zum Firestore. Dafür benötigt man die Datei *serviceAccount.json*, die man in Firestore Konsole findet.

## 2. serviceAccount.json
Siehe 1

## 3. firebase_to_elastic.ipynb
Dieses Programm bekommt die Daten vom Firestore, filtert sie, schickt die gefilterten Daten zum Elasticstore und erstellt Indexe, Dataviews, Rollen und Dashboards.

## 4. Dashboards.ndjson
Hier findet man die fünf Dashboards exportiert, die wir erstellt haben.

## 5. plz_geocoord.csv
Diese Datei ist wichtig, um die Standorte der User mittels PLZ zu ermitteln.

## 6. new_dashboards 
Diese Datei wird nach der Ausführung befüllt, um Dashboards für verschiedene Origsnisationen zu erstellen. 
