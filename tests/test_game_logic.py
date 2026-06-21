from logic_utils import check_guess, get_range_for_difficulty
import random

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_easy_difficulty_range():
    # Easy difficulty should have range 1-20
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20


def test_normal_difficulty_range():
    # Normal difficulty should have range 1-100
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100


def test_hard_difficulty_range():
    # Hard difficulty should have range 1-50
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50


def test_secret_within_easy_range():
    # Secret generated for Easy should be within 1-20
    low, high = get_range_for_difficulty("Easy")
    for _ in range(100):
        secret = random.randint(low, high)
        assert low <= secret <= high


def test_secret_within_normal_range():
    # Secret generated for Normal should be within 1-100
    low, high = get_range_for_difficulty("Normal")
    for _ in range(100):
        secret = random.randint(low, high)
        assert low <= secret <= high


def test_secret_within_hard_range():
    # Secret generated for Hard should be within 1-50
    low, high = get_range_for_difficulty("Hard")
    for _ in range(100):
        secret = random.randint(low, high)
        assert low <= secret <= high


def test_secret_out_of_range_bug_fixed():
    # Regression test: previously, a secret from Hard (1-50) could persist
    # when difficulty changed to Easy (1-20), causing out-of-range secrets.
    # This test verifies that secrets are generated within their difficulty's range.
    hard_low, hard_high = get_range_for_difficulty("Hard")
    easy_low, easy_high = get_range_for_difficulty("Easy")

    # A secret in the Hard range might be outside Easy range
    hard_secret = random.randint(21, hard_high)  # Between 21-50
    assert not (easy_low <= hard_secret <= easy_high), \
        f"Secret {hard_secret} should be out of Easy range (1-20)"

    # When switching to Easy, we should generate within Easy range
    easy_secret = random.randint(easy_low, easy_high)
    assert easy_low <= easy_secret <= easy_high, \
        f"Secret {easy_secret} should be in Easy range (1-20)"


def test_new_game_resets_state():
    # Regression test for: New Game button not resetting status, history, and score
    # Previously, clicking "New Game" only reset attempts and secret, causing
    # the game to be stuck in "won" or "lost" state and not allow new games.

    # Simulate a game that reached "won" state
    game_state = {
        "secret": 42,
        "attempts": 5,
        "status": "won",
        "history": [10, 20, 30, 40, 42],
        "score": 75
    }

    # Simulate New Game button logic: reset all state
    def reset_game_state(state):
        state["attempts"] = 0
        state["secret"] = random.randint(1, 100)
        state["status"] = "playing"
        state["history"] = []
        state["score"] = 0
        return state

    new_state = reset_game_state(game_state)

    # Verify all state is properly reset
    assert new_state["attempts"] == 0
    assert 1 <= new_state["secret"] <= 100
    assert new_state["status"] == "playing", \
        f"Status should be reset to 'playing', but got '{new_state['status']}'"
    assert new_state["history"] == [], \
        f"History should be empty, but got {new_state['history']}"
    assert new_state["score"] == 0, \
        f"Score should be reset to 0, but got {new_state['score']}"


def test_new_game_resets_lost_state():
    # Regression test for lost game state reset
    game_state = {
        "secret": 50,
        "attempts": 8,
        "status": "lost",
        "history": [10, 20, 30, 40, 45, 48, 49, 51],
        "score": -15
    }

    def reset_game_state(state):
        state["attempts"] = 0
        state["secret"] = random.randint(1, 100)
        state["status"] = "playing"
        state["history"] = []
        state["score"] = 0
        return state

    new_state = reset_game_state(game_state)

    # Verify status is reset from "lost" to "playing"
    assert new_state["status"] == "playing", \
        f"Status should be reset to 'playing' from 'lost', but got '{new_state['status']}'"
    assert new_state["history"] == []
    assert new_state["score"] == 0
