import pytest

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


# ---------- get_range_for_difficulty ----------

@pytest.mark.parametrize(
    "difficulty, expected",
    [
        ("Easy", (1, 20)),
        ("Normal", (1, 100)),
        ("Hard", (1, 50)),
    ],
)
def test_range_known_difficulties(difficulty, expected):
    assert get_range_for_difficulty(difficulty) == expected


@pytest.mark.parametrize("difficulty", ["", "easy", "Impossible", None])
def test_range_unknown_difficulty_defaults_to_normal(difficulty):
    assert get_range_for_difficulty(difficulty) == (1, 100)


# ---------- parse_guess ----------

@pytest.mark.parametrize(
    "raw, expected",
    [
        ("5", 5),
        ("0", 0),
        ("-3", -3),
        ("100", 100),
        ("7.9", 7),
        ("-2.5", -2),
        ("3.0", 3),
    ],
)
def test_parse_guess_valid(raw, expected):
    assert parse_guess(raw) == (True, expected, None)


@pytest.mark.parametrize("raw", [None, ""])
def test_parse_guess_empty(raw):
    assert parse_guess(raw) == (False, None, "Enter a guess.")


@pytest.mark.parametrize("raw", ["abc", "1.2.3", "5a", "--4", "  ", "nan", "inf"])
def test_parse_guess_not_a_number(raw):
    assert parse_guess(raw) == (False, None, "That is not a number.")


# ---------- check_guess ----------

@pytest.mark.parametrize(
    "guess, secret",
    [(50, 50), (1, 1), (100, 100), (0, 0)],
)
def test_check_guess_win(guess, secret):
    outcome, message = check_guess(guess, secret)
    assert outcome == "Win"
    assert "Correct" in message


@pytest.mark.parametrize(
    "guess, secret",
    [(60, 50), (51, 50), (100, 1), (0, -1)],
)
def test_check_guess_too_high(guess, secret):
    outcome, message = check_guess(guess, secret)
    assert outcome == "Too High"
    assert "LOWER" in message


@pytest.mark.parametrize(
    "guess, secret",
    [(40, 50), (49, 50), (1, 100), (-1, 0)],
)
def test_check_guess_too_low(guess, secret):
    outcome, message = check_guess(guess, secret)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# ---------- update_score ----------

@pytest.mark.parametrize(
    "attempt, expected_points",
    [
        (1, 80),   # 100 - 10 * 2
        (2, 70),
        (5, 40),
        (8, 10),   # exactly the floor
        (9, 10),   # would be 0, floored to 10
        (50, 10),  # far past the floor
    ],
)
def test_update_score_win_points(attempt, expected_points):
    assert update_score(0, "Win", attempt) == expected_points


def test_update_score_win_adds_to_current_score():
    assert update_score(25, "Win", 1) == 105


@pytest.mark.parametrize("outcome", ["Too High", "Too Low"])
def test_update_score_wrong_guess_penalty(outcome):
    assert update_score(50, outcome, 3) == 45


def test_update_score_wrong_guess_can_go_negative():
    assert update_score(0, "Too High", 1) == -5


@pytest.mark.parametrize("outcome", ["", "Unknown", None])
def test_update_score_unknown_outcome_unchanged(outcome):
    assert update_score(42, outcome, 3) == 42
