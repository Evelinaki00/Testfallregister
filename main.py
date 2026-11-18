
from test_case import TestCase
from test_case_register import TestCaseRegister


def main():
    register = TestCaseRegister()

    while True:
        print("\n===== TESTFALLSREGISTER =====")
        print("1. Registrera nytt testfall")
        print("2. Visa alla testfall")
        print("3. Avsluta")

        choice = input("Välj ett alternativ: ")

        if choice == "1":
            title = input("Ange titel: ")
            description = input("Ange beskrivning: ")
            expected_result = input("Ange förväntat resultat: ")

            test_case = TestCase(title, description, expected_result)
            register.add_test_case(test_case)

            print("Testfallet har registrerats!")

        elif choice == "2":

          if register.test_cases:
                register.show_all_test_cases()
          else:
                print("Det finns inga sparade testfall att visa.")

        elif choice == "3":
            print("Programmet avslutas.")
            break

        else:
            print("Ogiltigt val. Försök igen.")


main()
