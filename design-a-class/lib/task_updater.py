class Tasktracker():
    def __init__(self):
        #Parameters: None
        #Returns: None
        #Side effects: None
        self._tasks = []
        #creating an empty list at the start to add or remove tasks to/from


    def add(self, task):
        self.task = task
        if type(task) != str:
            raise Exception("Tasks must be passed as a string.") 
        self._tasks.append(task)
        return self.list_tasks()
    #Parameters: a string called task
    #Returns: A list of the tasks that have been added
    #Side effects: Will append the self.tasks list
    def list_tasks(self):
        return self._tasks


    def make_task_complete(self, task_name):
        del self._tasks[task_name]
        return self._tasks
    #Parameters: a task string which will be removed from the list of tasks
    #Returns: The list of remaining tasks once the passed task has been removed
    #Side effects: Removes the passed task from the list of tasks 