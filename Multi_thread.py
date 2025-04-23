from concurrent.futures import ThreadPoolExecutor, as_completed
from Modules.Main import scrape


def thread(system):
    print("I am here!")
    job_list = ["Data Engineer","Data Scientist","ETL Developer","Data Analyst"]

    with ThreadPoolExecutor(max_workers=2) as executor:
        jobs = [executor.submit(scrape, job,system) for job in job_list]

        for future in as_completed(jobs):
            print(f"Job done: {future.result()}")

thread("windows")