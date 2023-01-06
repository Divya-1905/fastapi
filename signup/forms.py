from typing import Optional
from pydantic import BaseModel
from fastapi import Request


class account(BaseModel):
    id:Optional[int]
    name:Optional[str]
    email:Optional[str]
    password:Optional[str]
    phone:Optional[str]


    class Config:
        orm_mode = True


class accountform:
    def __init__(self,request,Request):
        self.request:Request = request
        self.name:Optional[str]
        self.phone:Optional[str]
        self.email:Optional[str]
        self.password:Optional[str]
    def validate(self):
        if not self.name:
            raise ('name is requird')
        if self.email is not'@gmail.com':
            raise ('email is requird')
        if self.password is not len>10:
            raise ('password is requird')         
        