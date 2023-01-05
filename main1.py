from fastapi import FastAPI,status,HTTPException,Form
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
from models import accounts
import models
from database import engine

db=SessionLocal()
app=FastAPI()
database = engine
class Item(BaseModel): #serializer
    id:int
    name:str
    description:Optional[str]
    price:Optional[str]
    on_offer:bool

    class Config:
        orm_mode=True

class account(BaseModel):
    id:Optional[int]
    name:Optional[str]
    email:Optional[str]
    password:Optional[str]
    phone:Optional[str]

    class Config:
        orm_mode = True


@app.get('/items',response_model=List[Item],status_code=200)
def get_all_items():
    items=db.query(models.Item).all()

    return items

@app.get('/accounts',response_model=account,status_code=200)
def get_all_accounts():
    accounts=db.query(models.accounts).filter(models.accounts.email == 'user1@gmail.com').first()
    return accounts

@app.post('/signup/',response_model=account,status_code=status.HTTP_201_CREATED)
def signup(account:account):
    try:
        db_user = models.accounts(email=account.email, password= account.password,phone= account.phone,name=account.name)   
        db.add(db_user)    
        db.commit()   
        db.refresh(db_user)    
        return db_user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
    except:
        db.rollback()
        raise {'error'}
@app.put('/signupdate/{accounts_id}',status_code=status.HTTP_200_OK)
def update_account(accounts_id:int,acc:account):
    acc_to_uptodate = db.query(models.accounts).get(accounts_id)
    acc_to_uptodate.name = acc.name
    acc_to_uptodate.email = acc.email
    acc_to_uptodate.password = acc.password
    acc_to_uptodate.phone = acc.phone
    db.add(acc_to_uptodate)
    db.commit()
    db.refresh(acc_to_uptodate)
    return acc_to_uptodate

@app.delete('/accounts/{accounts_id}',status_code=status.HTTP_200_OK)
def deleteaccounts(accounts_id:int):
    acc_to_delete = db.query(models.accounts).get(accounts_id)
    if acc_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.add(acc_to_delete)
    db.delete(acc_to_delete)
    db.commit()
    return (status.HTTP_200_OK)










    
@app.get('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
def get_an_item(item_id:int):
    item=db.query(models.Item).filter(models.Item.id==item_id).first()
    return item

@app.post('/items',response_model=Item,
        status_code=status.HTTP_201_CREATED)
def create_an_item(item:Item):
    db_item=db.query(models.Item).filter(models.Item.name==item.name).first()

    if db_item is not None:
        raise HTTPException(status_code=400,detail="Item already exists")
    new_item=models.Item(
        name=item.name,
        price=item.price,
        description=item.description,
        on_offer=item.on_offer
    )
    db.add(new_item)
    db.commit()

    return new_item

@app.put('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
def update_an_item(item_id:int,item:Item):
    item_to_update=db.query(models.Item).filter(models.Item.id==item_id).first()
    item_to_update.name=item.name
    item_to_update.price=item.price
    item_to_update.description=item.description
    item_to_update.on_offer=item.on_offer

    db.commit()

    return item_to_update

@app.delete('/item/{item_id}')
def delete_item(item_id:int):
    item_to_delete=db.query(models.Item).filter(models.Item.id==item_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(item_to_delete)
    db.commit()

    return item_to_delete



