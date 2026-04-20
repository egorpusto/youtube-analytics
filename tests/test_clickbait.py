import pytest
from reports.clickbait import ClickbaitReport
from models import Video


@pytest.fixture
def sample_data():
    return [
        Video("A", 25.0, 22),
        Video("B", 22.5, 28),
        Video("C", 18.2, 35),
        Video("D", 16.5, 42),
        Video("E", 9.5, 82),
    ]


def test_clickbait_filter(sample_data):
    report = ClickbaitReport()
    result = report.generate(sample_data)

    assert all(v.ctr > 15 for v in result)
    assert all(v.retention_rate < 40 for v in result)


def test_clickbait_sorting(sample_data):
    report = ClickbaitReport()
    result = report.generate(sample_data)

    ctrs = [v.ctr for v in result]
    assert ctrs == sorted(ctrs, reverse=True)


def test_exact_result():
    data = [
        Video("A", 20, 30),
        Video("B", 10, 30),
    ]

    report = ClickbaitReport()
    result = report.generate(data)

    assert result == [Video("A", 20, 30)]


def test_ctr_boundary_not_included():
    data = [Video("A", 15.0, 30.0)]

    report = ClickbaitReport()
    result = report.generate(data)

    assert result == []


def test_retention_boundary_not_included():
    data = [Video("A", 20.0, 40.0)]

    report = ClickbaitReport()
    result = report.generate(data)

    assert result == []

def test_empty_data():
    report = ClickbaitReport()
    assert report.generate([]) == []