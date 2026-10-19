"""Save a list of scores to a text file, one per line."""


def save_scores(path: str, scores: list[int]) -> None:
    """Write each score on its own line in the file at path."""
    with open(path, "w") as file:
        for score in scores:
            file.write(str(score) + "\n")
