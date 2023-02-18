from src.pre_built.counter import count_ocurrences


def test_counter():
    count_ocurrences('data/jobs.csv', 'Python')
    assert type('data/jobs.csv') == str
    assert count_ocurrences('data/jobs.csv', 'Python') == 1639
