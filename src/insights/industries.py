from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs_list = read(path)
    job_industries_set = set()
    for job in jobs_list:
        if (job["industry"]):
            job_industries_set.add(job["industry"])
    return list(job_industries_set)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    indrustry_list = []
    for job in jobs:
        if job["industry"] == industry:
            new_dict = {}
            new_dict["id"] = job["id"]
            new_dict["industry"] = industry
            indrustry_list.append(new_dict)
    return indrustry_list
