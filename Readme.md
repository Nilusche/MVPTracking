
Dieses Repository besitzt Skripte, die Fakedaten generierts, sie zu Elastic Cloud schickt spezifische Anforderungen durch Tranformationen erfüllt, um explorativ Daten zu analysieren.

# Erklärung der Dateien

## 1. faker_firebase.ipynb und faker_firebase.py 
Dieses Program generiert Fakedaten mittels des Faker-Modul und schickt sie zu Firestore. Dafür benötigt man die Datei *serviceAccount.json*, die man in der Firestore Konsole findet.
Für die Pythondatei installiere die Bibliotheken mittels des Befehlts `pip install -r requirements.txt`

## 2. serviceAccount.json
Siehe 1

## 3. firebase_to_elastic.ipynb und firebase_to_elastic.py
Dieses Programm bekommt die Daten von Firestore, filtert sie, schickt die gefilterten Daten zum Elasticstore und erstellt Indices, Dataviews, Rollen und Dashboards. Für die Pythondatei installiere die Bibliotheken mittels des Befehlts `pip install -r requirements.txt`

## 4. Dashboards.ndjson
Hier findet man die fünf Dashboards exportiert, die wir erstellt haben.

## 5. plz_geocoord.csv
Diese Datei ist wichtig, um die Standorte der User mittels PLZ zu ermitteln.

## 6. new_dashboards 
Diese Datei wird nach der Ausführung befüllt, um Dashboards für verschiedene Origsnisationen zu erstellen. 

## Template files
Die `serviceAccountTemplate.json` repräsentiert wie die serviceAccount.json der Firestore Konsole aussehen wird. <br>
Die `.env.template` muss ersetzt werden durch eine .env Datei mit den Daten aus Elastic: <br>
<ol>
<li>ELASTIC_CLOUD_ID: Zu finden in "Manage this deployment"</li>
<li>ELASTIC_CLOUD_ID: Zu finden in "Manage this deployment" unter "Security"</li>
<li>ELASTIC_HOST: Zu finden in "Manage this deployment" Seite unter Kibana / copy endpoint</li>
<li>ELASTIC_PASSWORT: Nutzerpasswort, zurücksetzen unter "Manage this Deployment" -> Security / Reset password</li> 
</ol>
<img width="182" alt="image" src="https://github.com/majdbousaad/MVPTracking/assets/73897941/5f3f0dde-5987-4ad9-810c-1a4b3d7f17ed">

## Dockerfile
Diese Datei kann man optionalerweise verwenden um das Skript in einem Docker Container zum Laufen zu bringen
