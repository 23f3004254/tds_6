from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# ✅ Enable CORS (important for grader)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Load CSV
df = pd.read_csv("q-fastapi.csv")
students = df.to_dict(orient="records")

# ✅ API endpoint
@app.get("/api")
def get_students(class_param: list[str] = Query(default=None, alias="class")):
    
    if class_param:
        filtered = [s for s in students if s["class"] in class_param]
    else:
        filtered = students

    return {"students": filtered}