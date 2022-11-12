class TEST(object):
    @classmethod
    def query(cls, task=''):
        print(task)
        return task

    @classmethod
    def exec(cls, task=1):
        result = TEST.query(task)
        return result
