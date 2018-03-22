from pymongo import MongoClient
import pandas as pd

client = MongoClient()
client = MongoClient("mongodb://localhost:27017")


db = client.madatabase
collection = db.macollection

collection.find_one()

df = pd.read_csv("data/ks-projects-201801-sample.csv") 

objects = df.to_json(orient="records") # On tranforme en objet

collection.insert_many(objects)

#recupérer les 5 projets ayant reçu le plus de promesses de dons

collection.find().sort("pledged",-1).limit(5)






