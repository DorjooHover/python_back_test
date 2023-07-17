from fastapi import APIRouter

from models.user import User
from config.db import conn, db, collection
from schemas.user import serializeDict, serializeList
from bson import ObjectId 
user = APIRouter()

@user.get('/')
async def find_all_users():
 
  return serializeList(collection.find())
@user.get('/{id}')
async def find_one_user(id):
  return serializeDict(collection.find_one({
    "_id": ObjectId(id)}))
 
@user.post('/')
async def create_user(user: User):
  collection.insert_one(dict(user))
  return serializeList(collection.find())

@user.put('/{id}')
async def update_user(id, user: User):
  return serializeDict(collection.find_one_and_update({
    "_id": ObjectId(id)},{
      "$set": dict(user)
    
  }))
 
@user.delete('/{id}')
async def delete_user(id, ):
  return serializeDict(collection.find_one_and_delete({
    "_id": ObjectId(id)}))
 
