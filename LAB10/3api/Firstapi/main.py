from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

# สร้างโมเดล Pydantic สำหรับข้อมูลการสั่งซื้อพิซซ่า
class PizzaOrder(BaseModel):
    name: str
    size: str
    toppings: List[str]
    quantity: int

# ข้อมูลตัวอย่างสำหรับเมนูพิซซ่า
menu_items = {
    "pepperoni": {"name": "Pepperoni", "price": 10.99},
    "margherita": {"name": "Margherita", "price": 9.99},
    "vegetarian": {"name": "Vegetarian", "price": 11.99}
}

# เส้นทาง API สำหรับการสั่งซื้อพิซซ่า
@app.post("/order/")
async def place_order(order: PizzaOrder):
    # ตรวจสอบว่าเมนูที่สั่งอยู่ในรายการหรือไม่
    if order.name not in menu_items:
        raise HTTPException(status_code=404, detail="Menu item not found")
    
    # คำนวณราคาทั้งหมดของการสั่งซื้อ
    total_price = menu_items[order.name]["price"] * order.quantity
    
    # สร้างข้อความยืนยันการสั่งซื้อ
    confirmation_message = f"Order confirmed: {order.quantity} {order.size} {order.name} pizza(s) with {', '.join(order.toppings)}. Total price: ${total_price}"
    
    return {"message": confirmation_message}

# เส้นทาง API สำหรับการเรียกดูเมนูพิซซ่าทั้งหมด
@app.get("/menu/")
async def get_menu():
    return menu_items