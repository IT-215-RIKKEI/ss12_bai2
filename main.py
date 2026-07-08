from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from model import CustomerModel
from schema import CustomerUpdate, CustomerResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.put("/customers/{customer_id}", response_model=CustomerResponse)
def update_customer(customer_id: int, customer_update: CustomerUpdate, db: Session = Depends(get_db)):
    customer = db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    customer.full_name = customer_update.full_name
    customer.phone = customer_update.phone
    customer.address = customer_update.address
    db.commit()
    db.refresh(customer)
    return customer
