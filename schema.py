from pydantic import BaseModel

class CustomerUpdate(BaseModel):
    full_name: str
    phone: str
    address: str

class CustomerResponse(BaseModel):
    id: int
    full_name: str
    phone: str
    address: str

    class Config:
        from_attributes = True
