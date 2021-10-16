"""
This file will create my base inventory that can then be manipulated in the main file.
"""

# Begin with importing necessary modules
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# connect to database
cred = credentials.Certificate("CSE 310 non-Github items\service_key.json")
firebase_admin.initialize_app(cred)

# create shortcut to make life easier
db = firestore.client()

# create hats in hat collection
def create_data():
    """ This function will create the initial data for my data base. """
    # hat 1
    db.collection("Hats").document("H1").set({"Logo": "IdahoApex", "Brim": "Baseball","Size": "Flexfit; One size fits all.", 
    "Colors": "black, grey, forest green", "instock": True})

    # hat 2
    db.collection("Hats").document("H2").set({"Logo": "BrownGold", "Brim": "baseball", "Size": "Flexfit; One size fits all.", 
    "Colors": "black, grey, navy blue", "instock": True})

    # hat 3
    db.collection("Hats").document("H3").set({"Logo": "ElkShed", "Brim": "Snapback", "Size": "Adjustable; m-xl", 
    "Colors": "black, grey", "instock": True})

    # create shirts within the shirt collection

    # Shirt 1
    db.collection("Shirts").document("S1").set({"Logo": "IdahoApex", "Sizes": "Medium, Large, Extra Large", "Colors": 
    "black, grey, forest green, navy", "instock": True})

    # shirt 2
    db.collection("Shirts").document("S2").set({"Logo": "BrownGold", "Sizes": "Medium, Large, Extra Large", "Colors": 
    "black, grey, forest green", "instock": True})

    # Shirt 3
    db.collection("Shirts").document("S3").set({"Logo": "Elk cartoon", "Sizes": "Medium, Large, Extra Large", "Colors": 
    "black, grey, forest green, navy", "instock": True})

    # create Sweat Shirts

    # sweat shirt 1
    db.collection("Sweat Shirts").document("SW1").set({"Logo": "IdahoApex", "Sizes": "Medium, Large, Extra Large", 
    "Colors": "black, grey", "instock": True})

    # sweat shirt 2
    db.collection("Sweat Shirts").document("SW2").set({"Logo": "BrownGold", "Sizes": "Medium, Large, Extra Large", 
    "Colors": "black, grey", "instock": True})

create_data()