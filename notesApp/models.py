from django.db import models
from db_connection import db,mainDb
# Create your models here.

person_collection=db['Activity']
user_collection=db['users']

main_Activities = mainDb['Activities']
main_plot = mainDb['Plot']
main_ProjectMaster = mainDb['ProjectMaster']
main_Treatment = mainDb['Treatments']
main_Users = mainDb['Users']
