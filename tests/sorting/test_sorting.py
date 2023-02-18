from src.pre_built.sorting import sort_by
from src.insights.jobs import read


dict_list = read("data/jobs.csv")


def test_sort_by_criteria():
    sort_by(dict_list, "min_salary")
    assert dict_list[0]["id"] == "2191"
