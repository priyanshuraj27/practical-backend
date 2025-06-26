# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Route imports
from routes.learn import router as learn_router
from routes.invest import router as invest_router
from routes.save import router as save_router
from routes.earn import router as earn_router
from routes.chat import router as chat_router
app = FastAPI()

#  ADD CORS CONFIGURATION HERE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ Use "*" for dev only. Replace with specific IP/domain for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to Sakhi AI Backend"}

# routers
app.include_router(learn_router, prefix="/learn")
app.include_router(invest_router, prefix="/invest")
app.include_router(save_router, prefix="/save")
app.include_router(earn_router, prefix="/earn")
app.include_router(chat_router,prefix="/chat")
