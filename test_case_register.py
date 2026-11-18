
class TestCaseRegister:
    def __init__(self):
        self.test_cases = []

    def add_test_case(self, test_case):
        self.test_cases.append(test_case)

    def show_all_test_cases(self):
        for test_case in self.test_cases:
            test_case.display_test_case()
