from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    def __init__(self):
        BaseManager.__init__(address=("127.0.0.1", 50000), authkey=b"abc")
        self.connect()
        # self.task_queue =
        # self.result_queue =


if __name__ == "__main__":
    pass
