"""
Interactive Command-Line Runner for Python Starter Projects Suite
"""

from starter_suite import (
    caesar_cipher, change_email_domain, calculate_subnets,
    generate_password, pig_latin_translate, is_palindrome,
    is_leap_year, calculate_grade, count_frequency,
    count_digits, elevator_simulate, team_matchup
)

def show_menu():
    print("==================================================")
    print("      PYTHON STARTER PROJECTS UTILITY SUITE       ")
    print("==================================================")
    print("1. Caesar Cipher (Encode / Decode)")
    print("2. Email Domain Replacer")
    print("3. VLSM IP Subnet Calculator")
    print("4. Random Secure Password Generator")
    print("5. Pig Latin Translator")
    print("6. Palindrome Checker")
    print("7. Leap Year Evaluator")
    print("8. Academic Grading System")
    print("9. Frequency Counter")
    print("10. Elevator Simulator")
    print("11. Run Automated Demonstration")
    print("0. Exit")
    print("--------------------------------------------------")

def run_demo():
    print("\n[+] Running Quick Demo of All Utilities:")
    print("1. Caesar Cipher ('Hello World', shift=3) ->", caesar_cipher("Hello World", 3))
    print("2. Email Domain Change ('dev@company.com') ->", change_email_domain("dev@company.com", "company.com", "umat.edu.gh"))
    print("3. Password Generator ->", generate_password(14))
    print("4. Pig Latin ('python starter projects') ->", pig_latin_translate("python starter projects"))
    print("5. Palindrome Check ('racecar') ->", is_palindrome("racecar"))
    print("6. Leap Year (2024) ->", is_leap_year(2024))
    print("7. Academic Grade (85/100) ->", calculate_grade(85))
    print("8. Elevator Simulation (Current: 1 -> [5, 2]) ->", elevator_simulate(1, [5, 2]))
    print("9. Subnetting (192.168.1.0/24 for [50, 20 hosts]):")
    subnets = calculate_subnets("192.168.1.0/24", [50, 20])
    for s in subnets:
        print(f"   - Subnet: {s['allocated_subnet']} | Usable: {s['usable_range']}")

if __name__ == "__main__":
    run_demo()
