import pytest
from to_do import add_task, remove_task, display_tasks

# --- Fixture for a clean task list ---
@pytest.fixture
def empty_tasks():
    """Provides a fresh, empty list for each test."""
    return []

@pytest.fixture
def sample_tasks():
    """Provides a list with three tasks for removal tests."""
    return ["Buy groceries", "Water plants", "Pay bills"]

# ----------------------------------------------------
# 1. Tests for add_task(tasks, task)
# ----------------------------------------------------
def test_add_task_to_empty_list(empty_tasks):
    """Verifies a single task is correctly added to an empty list."""
    add_task(empty_tasks, "Study Python")
    assert empty_tasks == ["Study Python"]

def test_add_multiple_tasks(empty_tasks):
    """Verifies multiple tasks are added and maintain order."""
    add_task(empty_tasks, "Task A")
    add_task(empty_tasks, "Task B")
    assert empty_tasks == ["Task A", "Task B"]

def test_add_empty_task(empty_tasks):
    """Verifies an empty string task is technically allowed (valid use case)."""
    add_task(empty_tasks, "")
    assert empty_tasks == [""]

# ----------------------------------------------------
# 2. Tests for remove_task(tasks, task)
# ----------------------------------------------------
def test_remove_existing_task(sample_tasks):
    """Verifies an existing task is successfully removed."""
    remove_task(sample_tasks, "Water plants")
    assert sample_tasks == ["Buy groceries", "Pay bills"]

def test_remove_only_task(empty_tasks):
    """Verifies removing the last task leaves the list empty."""
    add_task(empty_tasks, "Only one task")
    remove_task(empty_tasks, "Only one task")
    assert empty_tasks == []

def test_remove_non_existent_task_raises_error(sample_tasks):
    """Tests that attempting to remove a task not in the list raises a ValueError."""
    # We use pytest.raises to assert that a specific exception is raised
    with pytest.raises(ValueError):
        remove_task(sample_tasks, "Wash car")

# ----------------------------------------------------
# 3. Tests for display_tasks(tasks) (Uses capsys to capture print output)
# ----------------------------------------------------
def test_display_empty_tasks(empty_tasks, capsys):
    """Tests the display function output for an empty list."""
    display_tasks(empty_tasks)
    
    # capsys captures everything printed to stdout
    captured = capsys.readouterr()
    
    # Expected output should only be the header
    expected_output = "Tasks:\n"
    assert captured.out == expected_output

def test_display_sample_tasks(sample_tasks, capsys):
    """Tests the display function output for a list with tasks."""
    display_tasks(sample_tasks)
    
    captured = capsys.readouterr()
    
    # Expected output must match the tasks list content, including newlines
    expected_output = (
        "Tasks:\n"
        "Buy groceries\n"
        "Water plants\n"
        "Pay bills\n"
    )
    assert captured.out == expected_output