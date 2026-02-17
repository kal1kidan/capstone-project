from src.themes import assign_theme



def test_theme_assignment_ui():
    nouns = ["app", "design"]
    theme = assign_theme(nouns)

    assert "User Interface & Experience" in theme


def test_theme_assignment_other():
    nouns = ["randomword"]
    theme = assign_theme(nouns)

    assert theme == "Other"
