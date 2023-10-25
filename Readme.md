# How to install

### Docker
1. open docker folder 
2. run ``` docker-compose up -d ```

this will make Elasticsearch (9200), logstash (5044) and kibana(5601) running

### Firebase
1. open Firebase folder
2. run ``` npm install ```
3. run ``` npm run build  ```



### Elasticstore
1. open Elasticstore folder
2. run ``` npm install ```
3. run ``` npm start  ```

This will make the pipeline from firestore to elasticstore. By me it worked: if I add a new collection in Firebase console, I get a notification in elasticstore telling ``` Added [doc@FfQRaL6WIdFoyJSSFevp]  ```. If I update it, it will say: ``` updated [doc@FfQRaL6WIdFoyJSSFevp]  ```

The file references.ts inside elasticstore is responsible for correcting the pipeline. 
More information: https://medium.com/@acupofjose/wondering-how-to-get-elasticsearch-and-firebases-firestore-to-play-nice-1d84553aa280 
