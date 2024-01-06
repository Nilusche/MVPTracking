# %%


# %% [markdown]
# You might need to restart your environment after installing the libraries

# %%
from datetime import datetime
import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv  
load_dotenv()

# %% [markdown]
# ## Authentifizierungsparameter

# %%
# Found in firestore under service Accounts / create new private key
SERVICE_ACCOUNT = "serviceAccount.json"
# Found in the 'Manage this deployment' page
CLOUD_ID = os.getenv("ELASTIC_CLOUD_ID")
# Found in the 'Management' page under the section 'Security'
API_KEY = os.getenv("ELASTIC_API_KEY")
# Found in the 'Manage this deployment' page under Kibana / copy endpoint 
HOST = os.getenv("ELASTIC_HOST")
# Found in the 'Manage this deployment' page under Sqcurity / Reset password 
ELASTIC_PASSWORT = os.getenv("ELASTIC_PASSWORD")


# %% [markdown]
# # Load Firebasedata

# %%
cred = credentials.Certificate(SERVICE_ACCOUNT)                                                                                                
firebase_admin.initialize_app(cred)

# %%
#get list of collections
db = firestore.client()
collections = [x.id for x in db.collections()]
print(collections)

# %%
master_classes = db.collection("Masterclasses").get()
users = db.collection("Users").get()
coaches = db.collection("Coaches").get()
events = db.collection("Events").get()
blogs = db.collection("Blogs").get()
snax = db.collection("Snax").get()
organizations = db.collection("Orga").get()

#convert to json
master_classes = [x.to_dict() for x in master_classes]
users = [x.to_dict() for x in users]
coaches = [x.to_dict() for x in coaches]
events = [x.to_dict() for x in events]
blogs = [x.to_dict() for x in blogs]
snax = [x.to_dict() for x in snax]
organizations = [x.to_dict() for x in organizations]

# %% [markdown]
# # Filter out Firebase fields

# %% [markdown]
# ### Users

# %%
#remove fields email, firstName, lifetime, refACID, role, surname from users
for user in users:
    user.pop('email', None)
    user.pop('firstName', None)
    user.pop('lifetime', None)
    user.pop('refACID', None)
    user.pop('role', None)
    user.pop('surname', None)

# %% [markdown]
# ### Coaches

# %%
#remove about, blogs, books, facebook, image, instagram, link,linkedin, podcasts from coaches
for coach in coaches:
    coach.pop('about', None)
    coach.pop('blogs', None)
    coach.pop('books', None)
    coach.pop('facebook', None)
    coach.pop('image', None)
    coach.pop('instagram', None)
    coach.pop('link', None)
    coach.pop('linkedin', None)
    coach.pop('podcasts', None)

# %% [markdown]
# ### Masterclasses

# %%
#remove fields, courseLessons, courseOverview, Description, filterTags, Progress, videoURL from master_classes
for master_class in master_classes:
    master_class.pop('courseLessons', None)
    master_class.pop('courseOverview', None)
    master_class.pop('Description', None)
    master_class.pop('filterTags', None)
    master_class.pop('Progress', None)
    master_class.pop('videoURL', None)

# %%
from enum import Enum

class Event_Type(Enum):
    ENROLL_COURSE = 0
    SAVE_COURSE = 1
    UNSAVE_COURSE = 2
    COMPLETE_COURSE = 3
    COMPLETE_LESSON = 4
    LOGIN = 5
    LOGOUT = 6
    BERATER_KONTAKT = 7
    SAVE_BLOG = 8
    UNSAVE_BLOG = 9
    SAVE_SNAC = 10
    UNSAVE_SNAC = 11
    

# %% [markdown]
# # Calculate additional metrics

# %% [markdown]
# # Write data to elastic

# %% [markdown]
# We will recalculate aggregate metrics

# %% [markdown]
# ### Users

# %% [markdown]
# Total Watchtime

# %%
#Total Watchtime
#itertae through each users and calculate total watchtime by aggregating the Progress propertie of Watched
for user in users:
    watchtime = 0
    for watched in user['Watched']:
        watchtime += int(watched['progress'].split(" ")[0])
    user['TotalWatchtime'] = watchtime

# %% [markdown]
# Courses enrolled

# %%
# for each users go through events and filter Event-Type = enroll_course and calculate total enrollments
for user in users:
    enrollments = 0
    for event in events:
        if event['Event-Type'] == Event_Type.ENROLL_COURSE.name:
            if event['User-Id'] == user['id']:
                enrollments += 1
    user['Age'] = datetime.today().year - int(user['Birthdate'].split("/")[0])
    user['Courses_enrolled'] = enrollments

# %% [markdown]
# Courses completed

# %%
# for each users go through events and filter Event-Type = complete_course and calculate "Courses_completed"
for user in users:
    courses_completed = 0
    for event in events:
        if event['Event-Type'] == Event_Type.COMPLETE_COURSE.name:
            if event['User-Id'] == user['id']:
                courses_completed += 1
    user['Courses_completed'] = courses_completed

# %% [markdown]
# Courses saved

# %%
# for each users go through events and filter Event-Type = save_course and calculate "Courses_saved"
for user in users:
    courses_saved = 0
    for event in events:
        if event['Event-Type'] == Event_Type.SAVE_COURSE.name:
            if event['User-Id'] == user['id']:
                courses_saved += 1
    user['Courses_saved'] = courses_saved

# %% [markdown]
# <span style="color:#BAE1FF">Adding the locations from the csv to each user</span>

# %%
geotable = 'plz_geocoord.csv'

df = pd.read_csv(geotable)
df.set_index('plz', inplace=True)
df.head()

for user in users:
   if user['postalCode'] not in df.index:
       print(user['postalCode'])
       continue
       
   postalcode = int(str(user['postalCode']))
   
   user['geo'] =  {'location': str(df.loc[postalcode]['lat'])+","+str(df.loc[postalcode]['lng'])}



# %% [markdown]
# ### Events

# %%
for event in events:
    date = datetime.strptime(event['Timestamp'], '%Y/%m/%d').date()
    event['Year'] = date.year
    event['Month'] = date.month
    event['Day'] = date.day

# %% [markdown]
# Average session duration (maybe remove)

# %% [markdown]
# It is important to note that here we can calculate additional field metrics

# %% [markdown]
# # Move data to elastic

# %%

from elasticsearch import Elasticsearch


# Create the client instance
client = Elasticsearch(
    cloud_id=CLOUD_ID,
    api_key=API_KEY,
)
          

# %% [markdown]
# <span style="color:#BAE1FF">Adding geopoint as mapping to index users</span>

# %%
mappings = {
  "settings": {
    "number_of_shards": 1
  },
  "mappings": {
    "properties": {
      "geo": {
                  "properties": {
                     "location": {
                           "type": "geo_point"
                     }
                  }
               }
    }
  }
}


client.indices.create(index='users_all', body=mappings)
SECRET="Majd ist der Beste"

# %% [markdown]
# <span style="color:#BAE1FF">Add users</span>

# %%
for user in users:
    client.index(index="users_all", body=user, id=user["id"])


# %% [markdown]
# <span style="color:#BAE1FF">Add master classes</span>

# %%
for master_class in master_classes:
    client.index(index="masterclasses", body=master_class, id=master_class["id"])

# %% [markdown]
# <span style="color:#BAE1FF">Add blogs</span>

# %%
for blog in blogs:
    client.index(index="blogs", body=blog, id=blog["id"])

# %% [markdown]
# <span style="color:#BAE1FF">Add snax</span>

# %%
for snak in snax:
    client.index(index="snax", body=snak, id=snak["id"])

# %% [markdown]
# <span style="color:#BAE1FF">Add coaches</span>

# %%
for coach in coaches:
    client.index(index="coaches", body=coach, id = coach["id"])

# %% [markdown]
# <span style="color:#BAE1FF">Add events</span>

# %%
for event in events:
    client.index(index="events", body=event, id = event["Event-ID"])


# %% [markdown]
# # Creating Orga Indicies 

# %%
def get_schulen_users():
    result = []
    for user in users:
        if user["Education"] == "Schule":
            result += [user]
    return result

def get_orga_users(orga_name):
    result = []
    for user in users:
        if user["advisorACID"] == orga_name:
            result += [user]
    return result


# %%
mappings = {
  "settings": {
    "number_of_shards": 1
  },
  "mappings": {
    "properties": {
      "geo": {
                  "properties": {
                     "location": {
                           "type": "geo_point"
                     }
                  }
               }
    }
  }
}



def create_index(users, index_name):
    client.indices.create(index=index_name, body=mappings)
    for user in users:
        client.index(index=index_name, body=user, id=user['id'])


# %% [markdown]
# # Für Schüler

# %%
schueler = get_schulen_users()
create_index(schueler, "users_schueler")

# %% [markdown]
# # Für Organisationen

# %%
threshold = 11
big_organisations = []
for orga in organizations:
    name = orga["name"]

    if name not in ["Allianz",
    "Deutsche Bank",
    "Axa", "Orga_1"]:
        continue

    if "Schule" in name:
        continue

    people = get_orga_users(name)
    '''
    if len(people) < threshold:
        print(name)
        continue
    '''
    big_organisations += [name]


# %%
for name in big_organisations:
    people = get_orga_users(name)
    create_index(people, "users_" + "_".join(name.lower().split(" ")))


# %%
import requests
import json


search_url = HOST + "/api/saved_objects/_find?type=dashboard&search_fields=title&search="
export_url = HOST + "/api/saved_objects/_export"
import_url = HOST + "/api/saved_objects/_import?createNewCopies=True"
data_view_api = HOST + "/api/data_views/data_view"
space_api = HOST + "/api/spaces/space"


def post_request(url, json, headers = None):
    if headers is None:
        headers = {'kbn-xsrf': 'true'}
    s = requests.post(url, auth=('elastic', ELASTIC_PASSWORT), json=json, headers=headers)
    print(s.text)

def create_space(name):
    url = space_api
    data = {
        "id": build_index_name(name),
        "name": name,

    }
    post_request(url, data)

def change_export(export, new_index, organaisation_name, new_view_id, new_dashboard_title=None):
    data = export.split("\n")

    index_pattern = json.loads(data[0])
    dashboard = json.loads(data[1])
    third = json.loads(data[2])
    new_data = [index_pattern, dashboard, third]

    index_pattern["attributes"]["name"] = "Users " + organaisation_name
    index_pattern["attributes"]["title"] = new_index

    index_pattern["id"] = new_view_id

    if new_dashboard_title is not None:
        dashboard["attributes"]["title"] = new_dashboard_title
    else:
        dashboard["attributes"]["title"] = dashboard["attributes"]["title"][0:-12] + " ["+organaisation_name+"]"
    
    for item in dashboard["references"]:
        item["id"] = new_view_id
        
    new_data[0] = json.dumps(index_pattern)
    new_data[1] = json.dumps(dashboard)
    new_data[2] = json.dumps(third)

    new_data = "\n".join(new_data)
    file_name = dashboard["attributes"]["title"]
    file_path = "new_dashboards/" + file_name + ".ndjson"
    f = open(file_path, "w")
    f.write(new_data)
    return file_path

def get_dashboard_id(dashboard_name):
    url = search_url + dashboard_name
    r = requests.get(url, auth=('elastic', ELASTIC_PASSWORT))
    return r.json()["saved_objects"][0]["id"]

def get_dashboard_export(id):
    objects = [{
        "type": "dashboard",
        "id": id
    }]

    date = {
        "objects":objects,
        "includeReferencesDeep": "true"
    }
    headers = {'kbn-xsrf': 'true', "Content-Type" : "application/json"}

    export = requests.post(export_url, auth=('elastic', ELASTIC_PASSWORT), json=date, headers=headers)
    return export.text


def import_new_export(file_path, space):
    headers = {'kbn-xsrf': 'true'}
    url = HOST + "/s/" + space + "/api/saved_objects/_import?overwrite=True"
    s = requests.post(
        url, 
        auth=('elastic', ELASTIC_PASSWORT), 
        files={'file': open(file_path,'rb')}, 
        headers=headers
        )
    print(s.text)


def create_dataview(name, index, space=None):
    data = {
        "data_view": {
            "id": "dv_" + build_index_name(name),
            "title": index,
            "name": "Users " + name,
            "namespaces": [space] if space is not None else []
        }
    }
    headers = {'kbn-xsrf': 'true'}
    url = data_view_api
    s = requests.post(url, auth=('elastic', ELASTIC_PASSWORT), json= data, headers=headers)
    print(s.text)
def get_data_view(name):
    id =  "dv_" + build_index_name(name)
    url = HOST + "/s/"  + build_index_name(name) + "/api/data_views/data_view/" + id
    return requests.get(url, auth=('elastic', ELASTIC_PASSWORT)).json()

def get_space(name):
    url = space_api + "/" + build_index_name(name)
    s = requests.get(url, auth=('elastic', ELASTIC_PASSWORT))
    print(s.json())

def build_index_name(name):
    return str("_".join(name.lower().split(" ")))


def add_read_only_role(space):
    url = HOST + "/api/security/role/readonly_" + space
    data = {
        "elasticsearch": {
            "indices": [
                {
                    "names": [ "users_" + space],
                    "privileges": [ "read" ]
                }
            ]
        },
        "kibana" : [ {
            "feature" : {
                "dashboard" : ["read"]
            },
            "spaces" : [space]
         }]
    }
    
    
    headers = {'kbn-xsrf': 'true'}
    s = requests.put(url, auth=('elastic', ELASTIC_PASSWORT), json=data, headers=headers)
    print(s.text)




    


# %% [markdown]
# ## Create Spaces

# %%
for name in big_organisations:
    create_space(name)

# %% [markdown]
# ##  Create Date-views

# %%
for name in big_organisations:
    create_dataview( name, "users_" + build_index_name(name), build_index_name(name))

# %% [markdown]
# ## Create Dashboards

# %%
DASHBOARDS = [
    "\"Geographische Analysen [All Users]\"",
    "\"Analysen mit soziodemographischen Filtern [All Users]\"",
    "\"Soziodemographische Analyen ohne Filter [All Users]\""
]

IDS = []
for dashboard in DASHBOARDS:
    IDS +=  [get_dashboard_id(dashboard)]



for name in big_organisations:

    data_view_id = get_data_view(name)["data_view"]["id"]
    print(data_view_id)
    for dashboard in DASHBOARDS:
        id = get_dashboard_id(dashboard)
        export = get_dashboard_export(id)
        new_export = change_export(
            export, 
            new_index="users_" + build_index_name(name),
            organaisation_name= name,
            new_view_id= data_view_id 
            )
        import_new_export(new_export, build_index_name(name))
   

# %% [markdown]
# ## Create Roles

# %%
for name in big_organisations:
    add_read_only_role(build_index_name(name))



