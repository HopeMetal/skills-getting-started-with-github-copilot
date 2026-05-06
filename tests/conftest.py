import copy
import pytest
from src import app


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the global activities dictionary to its initial state before each test."""
    initial_activities = copy.deepcopy(app.activities)
    yield
    app.activities = copy.deepcopy(initial_activities)