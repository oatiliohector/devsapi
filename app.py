from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def main():
    return {"Welcome to the devpsAPI!": "Know more about on the route /docs"}

@app.get('/api/jobs/{job_id}')
def get_job(job_id: int):
    return {"job_id": job_id, "job_title": "Software Engineer", "company": "Devps"}