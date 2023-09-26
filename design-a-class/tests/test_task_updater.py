import pytest
from lib.task_updater import *

"""
Test to see that we are adding a task as a string
"""
def test_to_see_task_added_is_a_string():
    tasktrial = Tasktracker()
    with pytest.raises(Exception) as error:
        tasktrial.add(1234)
    assert str(error.value) == "Tasks must be passed as a string."

"""
Test to see we are being returned a list 
when add method is called with a string
"""

def test_to_return_list_from_add_when_called_with_string():
    tasktrial = Tasktracker()
    assert tasktrial.add("Finish this test") == ["Finish this test"]


"""
Test to see we are deleting a task from the list 
when calling make_task_complete
"""
def test_to_delete_single_task_from_list():
    tasktrial = Tasktracker()
    tasktrial.add("Finish this class test")
    tasktrial.add("Do Yoga")
    tasktrial.add("Read French")
    assert tasktrial.make_task_complete(2) == ["Finish this class test", "Do Yoga"]