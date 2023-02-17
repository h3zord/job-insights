from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs_list = read(path)
    salary_list = []
    for salary in jobs_list:
        if salary["max_salary"].isdigit():
            salary_list.append(int(salary["max_salary"]))
    return max(salary_list)


def get_min_salary(path: str) -> int:
    jobs_list = read(path)
    salary_list = []
    for salary in jobs_list:
        if salary["min_salary"].isdigit():
            salary_list.append(int(salary["min_salary"]))
    return min(salary_list)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError

    try:
        int(salary) and int(job["min_salary"]) and int(job["max_salary"])
    except TypeError:
        raise ValueError

    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError

    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
