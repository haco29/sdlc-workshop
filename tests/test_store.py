from poll import store
from poll.core import create_poll, vote


def test_load_returns_none_when_nothing_is_saved(tmp_path):
    assert store.load(tmp_path / "poll.json") is None


def test_save_then_load_round_trips_the_poll(tmp_path):
    path = tmp_path / "poll.json"
    poll = vote(create_poll("Lunch?", ["Pizza", "Sushi"]), "Pizza")

    store.save(poll, path)

    assert store.load(path) == poll


def test_clear_removes_the_saved_poll(tmp_path):
    path = tmp_path / "poll.json"
    store.save(create_poll("Lunch?", ["Pizza", "Sushi"]), path)

    store.clear(path)

    assert store.load(path) is None


def test_clear_is_safe_when_nothing_is_saved(tmp_path):
    store.clear(tmp_path / "poll.json")
