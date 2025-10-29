from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
def list_items():
    return {"items": ["book", "pen"]}
@router.post("/items")
def create_item(name: str, quantity: int):
    return {"message": f"Item {name} with quantity {quantity} created"}
@router.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item": {"id": item_id, "name": "sample item", "quantity": 10}}
@router.put("/items/{item_id}")
def update_item(item_id: int, name: str = None, quantity: int = None):
    return {"message": f"Item {item_id} updated with name {name} and quantity {quantity}"}
@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}
@router.get("/inventory-status")
def inventory_status():
    return {"status": "All systems operational"}    
@router.get("/suppliers")
def list_suppliers():
    return {"suppliers": ["Supplier A", "Supplier B"]}
@router.post("/suppliers")
def add_supplier(name: str, contact_info: str):
    return {"message": f"Supplier {name} added with contact info {contact_info}"}
@router.get("/categories")                  
def list_categories():
    return {"categories": ["Electronics", "Furniture", "Clothing"]}
@router.post("/categories")
def add_category(name: str):
    return {"message": f"Category {name} added"}
@router.get("/locations")
def list_locations():
    return {"locations": ["Warehouse 1", "Warehouse 2"]}
@router.post("/locations")
def add_location(name: str, address: str):
    return {"message": f"Location {name} added with address {address}"}
@router.get("/reports")
def generate_report(report_type: str):
    return {"report": f"{report_type} report generated"}
@router.get("/stock-levels")
def stock_levels():
    return {"stock_levels": {"item_1": 100, "item_2": 50}}
@router.post("/restock-item")
def restock_item(item_id: int, quantity: int):
    return {"message": f"Item {item_id} restocked with quantity {quantity}"}

