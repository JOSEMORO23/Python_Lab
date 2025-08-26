# backend/app/api.py

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.models import PredictRequest, PredictResponse
from app.predict import predict_fake_news
from app.auth import create_access_token, get_current_user
from app.users import verify_password, get_user
from datetime import timedelta

router = APIRouter()

# 🔐 Login: genera y retorna token JWT
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        return {"error": "Credenciales inválidas"}
    token = create_access_token(data={"sub": user["username"]}, expires_delta=timedelta(minutes=30))
    return {"access_token": token, "token_type": "bearer"}

# 🔒 Endpoint protegido
@router.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest, current_user: dict = Depends(get_current_user)):
    result = predict_fake_news(request.title, request.text)
    return PredictResponse(**result)

@router.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest, current_user: dict = Depends(get_current_user)):
    if not request.title.strip() or not request.text.strip():
        raise HTTPException(status_code=400, detail="Title and text must not be empty")
    result = predict_fake_news(request.title, request.text)
    return PredictResponse(**result)

