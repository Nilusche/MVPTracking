# %% [markdown]
# # Config

# %%


# %%
import firebase_admin
from firebase_admin import credentials, firestore
from faker import Faker
import numpy as np
from dotenv import load_dotenv
import os
load_dotenv()

# %%
cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)

# %% [markdown]
# # Checkout the collections and documents

# %%
#get list of collections
db = firestore.client()
collections = [x.id for x in db.collections()]
fake = Faker()
print(collections)

# %% [markdown]
# <h1 style="color:yellow">Constants from Dagmarverse</h1>

# %%
CLASSROOMS = [
    "Job",
    "Geld für morgen",
    "Partnerschaft",
    "Gründung",
    "Familie",
    "Investieren",
    "Ausbildung"
]

MASTERCLASSES = [
    "Unternehmensführung mit leichtem Gepäck",
    "Unternehmer-Mindset - Tätigkeiten auslagern",
    "Tipps & Tricks zu Content Creation",
    "Sicher in dein Bewerbungsgespräch",
    "Was ist Selbstwertgefühl - Die Auswirkungen auf Beziehung & Karriere und wie du es verbessern kannst 6 Fachwissen Vertrieb",
    "Die Immobilie als Altersvorsorge: Rechtliche Tipps für mehr finanzielle Sicherheit",
    "Wie funktionieren Versicherungen?",
    "Versicherung für Student:innen",
    "Mindset Vertrieb",
    "Immobilien-Verkauf Basics"
]

SNAX = [
    "Was muss ich bei der Versandverpackung meiner Produkte beachten?",
    "Wie sichere ich die Zukunft meines Kindes ab?",
    "Wie sichere ich meinen Online-Shop rechtlich ab?",
    "Wie informiere ich mich über finanzielle Entlastungsmöglichkeiten?",
    "Soll ich mein Depot bei einer Bank oder über eine App eröffnen?",
    "In welche ETFs sollte ich investieren?",
    "Wofür brauche ich ein Depot?",
    "Welches Budget sollte ich für SEA Marketing einplanen?",
    "Wie gehe ich mit unschöner Post um?",
    "Was für eine Domain soll ich für meinen Online-Shop nehmen?",
    "Was ist die Gender Pension Gap?",
    "Was muss ich beim Abschluss einer Haftpflichtversicherung beachten?",
    "Welche Versicherungen brauche ich für meine Wohnung?",
    "Wie viele Schulden darf ich beim Gründen machen?",
    "Der erste Schritt zur Gründung",
    "ETF oder Aktie?",
    "Wann sollte ich anfangen zu investieren?",
    "Lea Mishras größter Fehler beim Investieren",
    "Was sollte ich beim Investieren in Kryptowährungen beachten? 20 Persönliche Finanzen und Glück",
    "Wie komme ich an Tipps für mein Gründungsunternehmen?",
    "Was nützt mir eine Personal Brand?",
    "Wie Mahabat ihr Business gestartet hat",
    "Wie kann ich meine Chancen auf dem Arbeitsmarkt verbessern?",
    "Mahabats Tipp für Gründer*innen"  
]

BLOGS = [
    {"title": "Finanzplanung leicht gemacht: Die 50:30:20 Regel", "author": "dagmar"},
    {"title": "Die Börse im Überblick", "author": "dagmar"},
    {"title": "Die 5 Grundregeln des Investierens", "author": "dagmar"},
    {"title": "Betriebliche Altersvorsorge (bAV): Überblick und Formen", "author": "dagmar"},
    {"title": "Mehr als nur Geld: Warum Selbstfürsorge der Schlüssel zur finanziellen Zufriedenheit ist", "author": "dagmar"},
    {"title": "Haushaltsbuch: Dein Schlüssel zu finanzieller Kontrolle und Unabhängigkeit", "author": "dagmar"},
    {"title": "Der Cost-Average-Effekt: Kluger Weg zur langfristigen Investition", "author": "dagmar"},
    {"title": "Die Verbesserten KfW-Fördermöglichkeiten für Familien in 2023", "author": "PHI"},
    {"title": "Was Selbstsändige von der Steuer absetzen können: Elne Übersicht", "author": "dagmar"},
    {"title": "Immobilien geerbt: Diese Fragen solltest du dir jetzt stellen", "author": "PHI"},
    {"title": "Größeres Angebot, Bessere Kaufchance für Immobilien?", "author": "PHI"},
    {"title": "Die 5 Pflichten des Immobilieneigentümers", "author": "PHI"},
    {"title": "Checkliste: Welche Unterlagen brauche ich für die Immobilienfinanzierung?", "author": "PHI"},
    {"title": "Scheitern ist kein Weltuntergang!", "author": "Coralie Richter"},
    {"title": "Scheitern ist menschlich", "author": "Coralie Richter"},
    {"title": "Im Scheitern liegt das Glück", "author": "Coralie Richter"},
    {"title": "Die Möglichkeiten sind grenzenlos", "author": "Coralie Richter"},
    {"title": "Traden vs. Langfristiges Investieren in Aktien: 2 Wege, ein Ziel", "author": "Emilia Bolda"},
    {"title": "Von Bullen und Bären - die faszinierende Sprache der Börse", "author": "Emilia Bolda"},
    {"title": "Impact Investing - Investieren mit positivem Einfluss", "author": "Emilia Bolda"},
    {"title": "Lerne in 10 Schritten wie die Börse funktioniert", "author": "Emilia Bolda"},
    {"title": "Die 5 häufigsten Fehler beim Aktienkauf", "author": "Emilia Bolda"}
]

AUTOREN = [
    "Holger Stollenwerk",
    "Lily Airich",
    "Gonzalo Agusti Cordano",
    "Jan P. & Alexander W.",
    "Bilgehan Karatas",
    "Matthias Rummler",
    "Achim Stollenwerk",
    "Bilgehan Karatas",
    "PHI Immobilien"
]

ORGANIZATIONS =[
    "Allianz",
    "Deutsche Bank",
    "Axa",
    "Schule_1",
    "Schule_2",
    "Schule_3",
    "Orga_1",
    "Orga_2"
    
]

ORGANIZATIONS_length = len(ORGANIZATIONS) - 1

MIN_DAUER = 5
MAX_DAUER = 3 * 60

autoren_length = len(AUTOREN) - 1
classrooms_length = len(CLASSROOMS) - 1
SNAX_length = len(SNAX) - 1
BLOGS_length = len(BLOGS) - 1


masterclasses_length = len(MASTERCLASSES) - 1

def get_random_master_class():
    return MASTERCLASSES[fake.random_int(max = masterclasses_length)]

def get_random_blog():
    return BLOGS[fake.random_int(max = BLOGS_length)]["title"]

def get_random_Snac():
    return SNAX[fake.random_int(max = SNAX_length)]


# %% [markdown]
# # Generate fake data and load into firestore

# %% [markdown]
# ### Masterclasses Collection

# %%
masterclassCollection = db.collection('Masterclasses')

list_of_levels = ["Basic", "Medium", "Advanced"]
list_of_status = ["locked", "unlocked", "completed"]

# %%



for i in range(len(MASTERCLASSES)):
    title = MASTERCLASSES[i]
    classrooms =  [CLASSROOMS[fake.random_int(max=classrooms_length)] for i in range(fake.random_int(2, 3))]
    autor = AUTOREN[fake.random_int(max=autoren_length)]
    id = i + 1
    level = list_of_levels[fake.random_int(0, 2)]
    points = 0
    if level == "Basic":
        points = points = fake.random_int(5, 10) * 10
    elif level == "Medium":
        points = points = fake.random_int(18, 21) * 10
    else:
        points = points = fake.random_int(30, 35) * 10
    data = {
        "art": "Masterclass",
        "author": autor,
        "classroom" : classrooms,
        "courseLessons" : [fake.random_int(1, 5) for i in range(fake.random_int(1, 5))],
        "courseOverview": {"AboutAuthor" : fake.text(50) + "...", "AboutCourse" : fake.text(50) + "..."},
        "description" : fake.text(max_nb_chars=50) + "...",
        "duration" : fake.random_int(MIN_DAUER, MAX_DAUER),
        "filterTags": classrooms,
        "id": id,
        "lessons": fake.random_int(1, 100),
        "level": level,
        "points": points,
        "progress": 0,
        "status": list_of_status[fake.random_int(0, 2)],
        "tags" : classrooms,
        "thumbnail" : fake.image_url(["facebook"]),
        "title" : title,
        "videoUrl" : fake.url(["video"]),
        "enrollment_count": fake.random_int(0, 100)
    }
    #masterclassCollection.add(data)
    print(data)


# %%
import random
usersCollection = db.collection('Users')

list_of_account_Types = ["admin", "master", "superadmin", "instructor"]
list_of_Education = ["Schule", "Abitur", "Realschulabschluss", "Hochschulabschluss", "Bachelor", "Master", "Promotion", "Ausbildung"]



Berlin = [10115,10117,10119,10178,10179, 10243,10245,10247,10249 ,10405,10407,10409,10435,10437,10439, 12679,12681,12683,12685,12687,12689 , 13347,13349,13351,13353,13355,13357,13359]
Aachen = [52062, 52064, 52066, 52068, 52070, 52072, 52074, 52076, 52078]
Munich =  [	80538, 80539, 80799, 80801, 80802, 80803, 80804, 80805, 80807, 80939, 80335, 80634, 80636, 80637, 80638, 80639, 80797, 80809, 80992]
Cologne = [	50668, 50670, 50672, 50674, 	50667, 50668, 50670, 50672, 	50825, 50827]
Frankfurt = [	60325, 60431, 60486, 60487, 	60320, 60322, 60431, 60433, 60435, 	60310, 60311, 60312, 60313, 60318, 60322, 60329, 	60316, 60318, 60320, 60322, 60389, 60435]
Duesseldorf = [40547 ]
Leipzig =  [4109, 4357]
Stuttgart= [	70191, 70372, 70374, 70376, 70378, 70192, 70469, 70499, 	70173, 70174, 70176, 70178, 70180, 70182, 70184, 70188, 70190, 	70174, 70191, 70192, 70193, 	70184, 70186, 70188, 70190, 70327]
Hamburg = [	22111, 22113, 22115, 22117, 22119, 	20097, 20535, 20537, 22087, 22089, 22111, 	20354, 20355, 20357, 20359, 20459, 22767, 22769]
Essen = [45130, 45131, 45133, 45136, 45147, 45128, 45138, 45139, 	45136, 45138, 45139]
Hannover = [	30159, 30161, 30167, 30169, 30171, 30175, 	30519, 30521, 30539, 	30159, 30169, 30171, 30173, 30175, 30519]
Bonn = [53111, 53113, 53115, 	53123, 53125 ]
Dortmund = [	44135, 44137, 44139, 44141, 44143, 44145, 44147, 44149, 44225, 44227, 44263, 44329, 44339, 44369, 	44143, 44263, 44269, 44287, 44267, 44269, 44287]


CITIES = [
    {"name": "Munich", "PLZ": Munich},
    {"name": "Aachen", "PLZ": Aachen},
    {"name": "Berlin", "PLZ": Berlin},
    {"name": "Cologne", "PLZ": Cologne},
    {"name": "Frankfurt", "PLZ": Frankfurt},
    {"name": "Düsseldorf", "PLZ": Duesseldorf},
    {"name": "Leipzig", "PLZ": Leipzig},
    {"name": "Stuttgart", "PLZ": Stuttgart},
    {"name": "Hamburg", "PLZ": Hamburg},
    {"name": "Essen", "PLZ": Essen},
    {"name": "Hannover", "PLZ": Hannover},
    {"name": "Bonn", "PLZ": Bonn},
    {"name": "Dortmund", "PLZ": Dortmund},
]



cities_length = len(CITIES) - 1

## normal dirtibution for age
mu, sigma = 30, 6
s = np.random.normal(mu, sigma, 1000)
s = [int(number) for number in s]
birthdates = [fake.date_of_birth(minimum_age=number, maximum_age=number).strftime('%Y/%m/%d') for number in s]



for i in range(1000):
    city = CITIES[fake.random_int(max=cities_length)]
    course_enrolled = fake.random_int(0, 5)
    city_name = city["name"]
    plzS = city["PLZ"]
    plzS_length = len(plzS) - 1
    plz = plzS[fake.random_int(max=plzS_length)]

    interest = []
    for classroom in CLASSROOMS:
        interest += [{"classroom": classroom, "score": fake.random_int(max=100)}]


    orga = ORGANIZATIONS[fake.random_int(max = ORGANIZATIONS_length)]
    education = list_of_Education[fake.random_int(0, len(list_of_Education) - 1)]
    
    birth_date = birthdates[i]
    employment = ["unemployed", "employed"][fake.random_int(0, 1)]
    role = fake.job()
    income =fake.random_int(10000, 80000)
    if "Schule" in orga:
        education = "Schule"
        birth_date = fake.date_of_birth(minimum_age=12, maximum_age=18).strftime('%Y/%m/%d')
        role = "Schüler"
        employment = "unemployed"
        income = 0

    data = {
        "id": i + 2,
        "accType": "Customer" if random.random() < 0.95 else list_of_account_Types[fake.random_int(0, 3)],
        "advisor": fake.name(),
        "advisorACID": orga,
        "city": city_name,
        "email": fake.email(),
        "firstName": fake.first_name(),
        "joined": fake.date_between(start_date='-2y').strftime('%Y/%m/%d'),
        "lifetime" : fake.random_int(0, 5),
        "postalCode": plz,
        "refACID": "reference" + str(i),
        "role": role,
        "surname": fake.last_name(),
        "Gender": list(["Male", "Female"])[fake.random_int(0, 1)],
        "Income": income,
        "Birthdate": birth_date,
        "Education": education,
        "Employment_status": employment,
        "Watched": [ {"Masterclass" : fake.random_int(1, max=masterclasses_length + 1), "progress": str(fake.random_int(0, 500)) + " min"} for i in range(fake.random_int(0, 5))],
        "Interest": interest,
        "Total_Watchtime" : str(fake.random_int(0, 100000)) + " min",
        "Avg_session_duration": str(fake.random_int(0, 200)) + " min",
        "Courses_enrolled" : course_enrolled,
        "Courses_completed" : fake.random_int(0, course_enrolled),
        "course_saved": fake.random_int(0, course_enrolled + 5)
    }
    usersCollection.add(data)
    #print(data)

# %% [markdown]
# ### Coach Collection

# %%
#coachCollection = db.collection('Coaches')

for i in range(100): 
    data = {
        "about": fake.text(50),
        "blogs": [fake.text(50) + "..." for i in range(fake.random_int(1, 5))],
        "books": [fake.word() for i in range(fake.random_int(1, 5))],
        "facebook": fake.url(),
        "id": i+2,
        "image": [fake.name()+ ".jpg" for i in range(fake.random_int(1, 5))],
        "instagram": fake.url(["instagram"]),
        "linkedin": fake.url(["linkedin"]),
        "link": fake.url(),
        "masterclass": [{"name": fake.name()} for i in range(fake.random_int(1, 5))],
        "podcasts" : [{"position": fake.job(), "website": fake.url(), "xing": fake.url()} for i in range(fake.random_int(1, 5))],
        "Name": fake.name(),
        "position": fake.job()
    }
    #coachCollection.add(data)
    print(data)

# %%
import random
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



class Event:
    def __init__(self, ID, type, timestamp, user_id, info) -> None:
        self.ID = ID
        self.type = type
        self.timestamp = timestamp
        self.user_id = user_id
        self.info = info

    def toDict(self):
        return {
            "Event-ID": self.ID,
            "User-Id": self.user_id,
            "Timestamp":  self.timestamp,
            "Event-Type" : self.type,
            "Event-Specific-Information" : self.info
        }


def generate_new_event(id):
    
    first_round = []
   

    if random.random() < 0.10:
        first_round += [Event_Type.LOGIN, Event_Type.LOGOUT]
    if random.random() < 0.20:
        first_round += [Event_Type.SAVE_COURSE, Event_Type.SAVE_BLOG, Event_Type.SAVE_SNAC]
    if random.random() < 0.10:
        first_round += [Event_Type.ENROLL_COURSE]
    if random.random() < 0.05:
        first_round += [Event_Type.COMPLETE_LESSON]
    if random.random() < 0.025:
        first_round += [Event_Type.COMPLETE_COURSE]
    if random.random() < 0.025:
        first_round += [Event_Type.UNSAVE_COURSE, Event_Type.UNSAVE_BLOG, Event_Type.UNSAVE_SNAC]
    if random.random() < 0.025/2:
        first_round += [Event_Type.BERATER_KONTAKT]
    
    #print(first_round)
    first_round_length = len(first_round)
    
    if first_round_length == 0:
        return generate_new_event(id)
    
    event_name = first_round[fake.random_int(max=first_round_length - 1)].name
    

    info = ""
    if "COURSE" in event_name:
        info = get_random_master_class()
    elif "BLOG" in event_name:
        info = get_random_blog()
    elif "SNAC" in event_name:
        info = get_random_Snac()
    else:
        info = "Keine Informationen"
        
    return Event(
        ID=id,
        user_id=fake.random_int(max=99) + 2,
        timestamp=fake.date_between(start_date='-2y').strftime('%Y/%m/%d'),
        type=event_name,
        info=info
    )

print(generate_new_event(1).toDict())



# %%
#eventCollection = db.collection('Events')

from datetime import date

for i in range(200): 
    event = generate_new_event(i + 2).toDict()
    #eventCollection.add(event)
    print(event)


# %%
# nicht nutzen wegen täglichem Limit von Operationen
def delete_collection(coll_ref, batch_size):
    docs = coll_ref.list_documents(page_size=batch_size)
    deleted = 0

    for doc in docs:
        print(f"Deleting doc {doc.id} => {doc.get().to_dict()}")
        doc.delete()
        deleted = deleted + 1

    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)
#db = firestore.client()
#collections = [x for x in db.collections()]
#for collection in collections:
    #delete_collection(collection, 0)

# %% [markdown]
# ### Blogs Collection

# %%
blogsCollection = db.collection('Blogs')

# %%
fake = Faker()
for i in range(len(BLOGS)):
    blog = BLOGS[i]
    classroom = [CLASSROOMS[fake.random_int(max=classrooms_length)] for _ in range(fake.random_int(1, 3))]
    data = {
        "id": i+2,
        "title": blog["title"],
        "author": blog["author"],
        "about": fake.text(50),
        "details": fake.text(50),
        "image": fake.image_url(["facebook"]),
        "introduction": fake.text(50),
        "tags": classroom,
        "thumbnail": fake.image_url(["facebook"]),
        "image": fake.image_url(["facebook"]),
        "art":fake.word(),
        "classroom": classroom,   
        "duration": fake.random_int(1, 100),
        "blogData": fake.text(50),
        "date": fake.date(),
    }
    blogsCollection.add(data)
    #print(data)

# %% [markdown]
# ### Snax Collection

# %%
snaxCollection = db.collection('Snax')

# %%
for i in range(len(SNAX)):
    title = SNAX[i]
    classroom = [CLASSROOMS[fake.random_int(max=classrooms_length)] for _ in range(fake.random_int(1, 3))]
    data = {
        "id": i + 2,
        "title": title,
        "art": "Snax",
        "author": fake.name(),
        "description": fake.text(50),
        "videoUrl": fake.url(["video"]),
        "progress": fake.random_int(1, 100),
        "thumbnail": "/snax/" + fake.image_url(["facebook"]),
        "status": "unlocked",
        "classroom": classroom,
        "level": "Beginner",
        "duration": fake.random_int(1, 100),
    }
    snaxCollection.add(data)
    #print(data)

# %% [markdown]
# ## Organisation Collection

# %%
orgaCollection = db.collection('Orga')



# %%
for i in range(len(ORGANIZATIONS)):
    name = ORGANIZATIONS[i]
    data = {
        "id" : i + 2,
        "name" : name 
    }
    orgaCollection.add(data)
    #print(data)


