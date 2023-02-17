from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs_list = [job for job in jobs_reader]
    return jobs_list


def get_unique_job_types(path: str) -> List[str]:
    jobs_list = read(path)
    job_type_set = set()
    for job in jobs_list:
        if (job["job_type"]):
            job_type_set.add(job["job_type"])
    return list(job_type_set)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    job_type_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            new_dict = {}
            new_dict["id"] = job["id"]
            new_dict["job_type"] = job_type
            job_type_list.append(new_dict)
    return job_type_list
