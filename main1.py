from fastapi import FastAPI,status,HTTPException,Request,Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
from models import accounts,Item,profile
import models
from database import engine
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
db=SessionLocal()
app=FastAPI()
database = engine
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
class Item(BaseModel): #serializer
    id:int
    name:str
    description:Optional[str]
    price:Optional[str]
    on_offer:bool
    
    class Config:
        orm_mode=True

class serializeraccount(BaseModel):
    id:Optional[int]
    name:Optional[str]
    email:Optional[str]
    password:Optional[str]
    phone:Optional[str]
    # def is_valid(self):
    #     if in not self


    class Config:
        orm_mode = True



class postserializeraccount(BaseModel):
    # id:Optional[int]
    name:Optional[str]
    email:Optional[str]
    password:Optional[str]
    phone:Optional[str]
    # def is_valid(self):
    #     if in not self


    # class Config:
    #     orm_mode = True

class profileserializer(BaseModel):
    id:Optional[int]
    name:Optional[str]
    email:Optional[str]
    password:Optional[str]
    class Config:
        orm_mode = True


class profile_serializer(BaseModel):
    id:Optional[int]
    name:Optional[str]
    email:Optional[str]
    password:Optional[str]
    class Config:
        orm_mode = True

@app.get('/items',response_model=List[Item],status_code=200)
def get_all_items():
    items=db.query(models.Item).all()

    return items

@app.get('/accounts',response_model=serializeraccount,status_code=200,)
def get_all_accounts(request:Request):
    accounts=db.query(models.accounts).filter(models.accounts.email == 'user4@gmail.com').first()
    # return accounts
    # return templates.TemplateResponse( "signup.html",{"request": request,"id":accounts.id})



@app.get("/signup/",response_class=HTMLResponse)
def signup(request:Request):
      return templates.TemplateResponse( "signup.html",{"request": request})

@app.post('/signup-post/',response_model=postserializeraccount,status_code=status.HTTP_201_CREATED)
def signup(request:Request,account:postserializeraccount ):
    print(account)
    try:
        print(account)
        db_user = models.accounts(email=account.email, password= account.password,phone= account.phone,name=account.name) 
        print(db_user)
        db.add(db_user)    
        db.commit()   
        db.refresh(db_user)    
    except Exception as e:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
    return templates.TemplateResponse('signup.html',{"request":request})    
   


# @app.get('signupdate/{accounts_id}',response_class=HTMLResponse)
# def signupdate(accounts_id:int,request:Request):
    


@app.put('/signupdate/{accounts_id}',status_code=status.HTTP_200_OK)
def update_account(accounts_id:int,acc:serializeraccount):
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

@app.get('/profile',response_model=profileserializer,status_code=status.HTTP_200_OK)
def profile_all_get(self):
    profile = db.query(models=profile).all()
    return profile
# @app.post('/post-profile/',response_model=profileserializer,status_code=status.HTTP_201_CREATED)
# def post_profile(request:Request,profile:profile_serializer):
#     try:
#         profile = models.profile(name=profile.name,email = profile.email,password = profile.password)
#     except:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @app.put('/profile/{profile_id}',response_model=profileserializer,status_code=status)
# def put_profile(profile_id:int,profile:profile_serializer):
#     profile_update= db.query(models.profile).filter(models.profile.id==profile.id).first()
#     profile_update.name=profile.name
#     profile_update.email=profile.email
#     profile_update.password=profile.password
#     db.commit()
#     return profile_update
# @app.delete('/profile/{profile_id}') 
# def delete_profile(profile_id:int):
#     profile_delete= db.query(models.profile).filter(models.profile.id==profile_id).first()
#     if profile_delete is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")    
#     db.delete(profile_delete)
#     db.commit()
#     return profile_delete   
    