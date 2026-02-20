from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI()

# Enable CORS (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load CSV
df = pd.read_csv("q-fastapi.csv")

@app.get("/api")
def get_students(class_param: list[str] = Query(default=None, alias="class")):
    # If class filter is provided
    if class_param:
        filtered_df = df[df["class"].isin(class_param)]
    else:
        filtered_df = df

    # Convert to required format
    students = filtered_df.to_dict(orient="records")

    return {"students": students}



if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)