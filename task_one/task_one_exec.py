import logging
import os

log = logging.getLogger(__name__)


class TaskOne(object):

    @staticmethod
    def run(task):
        log.info("Started FIRST task")

        task_result = {}

        try:
            os.system('kubectl apply -f bb.yaml')

            task_result["status"] = "Success"

        except Exception as e:
            log.error("Error running task: {0}".format(task))
            task_result["status"] = "Failed"
        else:
            pass
        return task_result

    @staticmethod
    def child_task_type(task):
        return '\n\n***\n\n'

    @staticmethod
    def has_child_task(task):
        return False
