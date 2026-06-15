from logic_utils import check_guess

def test_winning_guess():
    # Verify that guessing the secret number results in a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # Verify that a guess above the secret returns "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # Verify that a guess below the secret returns "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"