from fastapi import FastAPI

app = FastAPI(
    title="Devs API",
    description="Software Engineer Jobs API",
    version="1.0.0",
)

@app.get('/')
def main():
    return {"Welcome to the devpsAPI!": "Know more about on the route /docs"}

@app.get('/api/jobs/{job_id}')
def get_job(job_id: int):
    return {"job_id": job_id, "job_title": "Software Engineer", "company": "Devs"}
