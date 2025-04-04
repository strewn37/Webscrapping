from concurrent.futures import ThreadPoolExecutor, as_completed
from Main import scrape

job_list = ["Data Engineer","Data Scientist","ETL Developer","Data Analyst"]

with ThreadPoolExecutor(max_workers=2) as executor:
    jobs = [executor.submit(scrape, job) for job in job_list]

    for future in as_completed(jobs):
        print(f"Job done: {future.result()}")


