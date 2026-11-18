
class TestCase:
    def __init__(self, title, description, expected_result):
        self.title = title
        self.description = description
        self.expected_result = expected_result

    def display_test_case(self):
        print(f"Titel: {self.title}")
        print(f"Beskrivning: {self.description}")
        print(f"Förväntat resultat: {self.expected_result}")
