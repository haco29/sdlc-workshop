import pytest

from poll.core import create_poll, format_share, leaders, shares, tally, total_votes, vote


def make_poll():
    return create_poll("Lunch?", ["Pizza", "Sushi", "Salad"])


def test_create_poll_starts_with_zero_votes():
    poll = make_poll()

    assert poll["question"] == "Lunch?"
    assert poll["options"] == ["Pizza", "Sushi", "Salad"]
    assert poll["votes"] == {"Pizza": 0, "Sushi": 0, "Salad": 0}


def test_create_poll_trims_whitespace_and_drops_blank_options():
    poll = create_poll("  Lunch?  ", [" Pizza ", "", "   ", "Sushi"])

    assert poll["question"] == "Lunch?"
    assert poll["options"] == ["Pizza", "Sushi"]


def test_create_poll_needs_a_question():
    with pytest.raises(ValueError, match="question"):
        create_poll("   ", ["Pizza", "Sushi"])


def test_create_poll_needs_two_options():
    with pytest.raises(ValueError, match="two options"):
        create_poll("Lunch?", ["Pizza", ""])


def test_create_poll_rejects_duplicate_options():
    with pytest.raises(ValueError, match="unique"):
        create_poll("Lunch?", ["Pizza", "Pizza"])


def test_vote_adds_one_vote_to_the_option():
    poll = vote(make_poll(), "Sushi")

    assert poll["votes"]["Sushi"] == 1
    assert poll["votes"]["Pizza"] == 0


def test_vote_leaves_the_original_poll_unchanged():
    original = make_poll()

    vote(original, "Pizza")

    assert original["votes"]["Pizza"] == 0


def test_vote_for_an_unknown_option_raises():
    with pytest.raises(ValueError, match="Unknown option"):
        vote(make_poll(), "Burgers")


def test_tally_keeps_the_order_options_were_created_in():
    poll = vote(vote(make_poll(), "Salad"), "Salad")

    assert tally(poll) == [("Pizza", 0), ("Sushi", 0), ("Salad", 2)]


def test_total_votes_counts_every_vote():
    poll = vote(vote(vote(make_poll(), "Pizza"), "Sushi"), "Pizza")

    assert total_votes(poll) == 3


def test_total_votes_is_zero_for_a_new_poll():
    assert total_votes(make_poll()) == 0


def test_shares_are_each_options_percent_of_all_votes():
    poll = vote(vote(vote(make_poll(), "Pizza"), "Pizza"), "Sushi")
    poll = vote(poll, "Salad")

    assert shares(poll) == [("Pizza", 50.0), ("Sushi", 25.0), ("Salad", 25.0)]


def test_shares_round_to_two_decimals():
    poll = vote(vote(vote(make_poll(), "Pizza"), "Sushi"), "Salad")

    assert shares(poll) == [("Pizza", 33.33), ("Sushi", 33.33), ("Salad", 33.33)]


def test_shares_give_an_option_with_no_votes_zero_while_others_have_votes():
    poll = vote(vote(make_poll(), "Pizza"), "Sushi")

    assert shares(poll) == [("Pizza", 50.0), ("Sushi", 50.0), ("Salad", 0.0)]


def test_shares_are_zero_for_a_new_poll():
    assert shares(make_poll()) == [("Pizza", 0.0), ("Sushi", 0.0), ("Salad", 0.0)]


@pytest.mark.parametrize(
    ("percent", "label"),
    [(0.0, "0%"), (50.0, "50%"), (12.5, "12.5%"), (33.33, "33.33%"), (100.0, "100%")],
)
def test_format_share_drops_trailing_zeros(percent, label):
    assert format_share(percent) == label


def test_leaders_is_the_option_with_the_most_votes():
    poll = vote(vote(make_poll(), "Sushi"), "Sushi")
    poll = vote(poll, "Pizza")

    assert leaders(poll) == ["Sushi"]


def test_leaders_includes_every_tied_option():
    poll = vote(vote(make_poll(), "Pizza"), "Salad")

    assert leaders(poll) == ["Pizza", "Salad"]


def test_leaders_is_empty_for_a_new_poll():
    assert leaders(make_poll()) == []
