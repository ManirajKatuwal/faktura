from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def list_users():
    return {"users": ["admin", "demo"]}
@router.post("/login")
def login(username: str, password: str):
    if username == "admin" and password == "test":
        return {"message": "Login successful"}
    return {"message": "Invalid credentials"}
@router.post("/logout")
def logout():
    return {"message": "Logout successful"}
@router.get("/roles")
def list_roles():
    return {"roles": ["admin", "editor", "viewer"]}
@router.get("/permissions")
def list_permissions():
    return {"permissions": ["read", "write", "delete"]}
@router.post("/reset-password")
def reset_password(email: str):
    return {"message": f"Password reset link sent to {email}"}
@router.post("/change-password")
def change_password(username: str, old_password: str, new_password: str):           
    if old_password == "oldpass":
        return {"message": "Password changed successfully"}
    return {"message": "Old password is incorrect"} 

