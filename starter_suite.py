"""
Python Starter Projects - Unified Core Suite
Contains clean, typed, and robust implementations of standard Python starter algorithms and utilities.
"""

import string
import random
import ipaddress
import math
from typing import List, Dict, Tuple, Union

# 1. Caesar Cipher
def caesar_cipher(text: str, shift: int, direction: str = 'encode') -> str:
    """Encode or decode text using the Caesar cipher."""
    if direction.lower() == 'decode':
        shift = -shift
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)

# 2. Email Domain Changer
def change_email_domain(email: str, old_domain: str, new_domain: str) -> str:
    """Replace an email's domain if it matches old_domain."""
    if "@" in email:
        username, domain = email.rsplit("@", 1)
        if domain.lower() == old_domain.lower():
            return f"{username}@{new_domain}"
    return email

# 3. Subnetting VLSM Calculator
def calculate_subnets(network_cidr: str, host_requirements: List[int]) -> List[Dict[str, Union[str, int]]]:
    """Calculate VLSM subnets for given network and host count requirements."""
    host_requirements = sorted(host_requirements, reverse=True)
    base_network = ipaddress.ip_network(network_cidr, strict=False)
    available_subnets = [base_network]
    results = []

    for hosts in host_requirements:
        needed_hosts = hosts + 2
        bits_needed = math.ceil(math.log2(needed_hosts)) if needed_hosts > 1 else 1
        prefix = 32 - bits_needed

        allocated = None
        for i, candidate in enumerate(available_subnets):
            if candidate.prefixlen <= prefix:
                subnets_list = list(candidate.subnets(new_prefix=prefix))
                allocated = subnets_list[0]
                available_subnets.pop(i)
                available_subnets.extend(subnets_list[1:])
                break

        if allocated:
            usable = list(allocated.hosts())
            results.append({
                "required_hosts": hosts,
                "allocated_subnet": str(allocated),
                "network_address": str(allocated.network_address),
                "broadcast_address": str(allocated.broadcast_address),
                "usable_range": f"{usable[0]} - {usable[-1]}" if usable else "N/A",
                "subnet_mask": str(allocated.netmask),
                "prefix_length": f"/{allocated.prefixlen}"
            })
        else:
            raise ValueError(f"Insufficient address space for {hosts} hosts in network {network_cidr}.")

    return results

# 4. Password Generator
def generate_password(length: int = 12, use_digits: bool = True, use_symbols: bool = True) -> str:
    """Generate a random secure password."""
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
    ]
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice("!@#$%^&*()"))
        
    while len(password) < length:
        password.append(random.choice(chars))
        
    random.shuffle(password)
    return "".join(password)

# 5. Pig Latin Converter
def pig_latin_translate(text: str) -> str:
    """Translate text to Pig Latin."""
    vowels = "aeiouAEIOU"
    words = text.split()
    translated = []
    for word in words:
        clean_word = "".join(c for c in word if c.isalnum())
        punct = "".join(c for c in word if not c.isalnum())
        if not clean_word:
            translated.append(word)
            continue
        if clean_word[0] in vowels:
            new_word = clean_word + "way"
        else:
            first_vowel = next((i for i, c in enumerate(clean_word) if c in vowels), None)
            if first_vowel is not None and first_vowel > 0:
                new_word = clean_word[first_vowel:] + clean_word[:first_vowel] + "ay"
            else:
                new_word = clean_word + "ay"
        translated.append(new_word + punct)
    return " ".join(translated)

# 6. Palindrome Checker
def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome (ignoring non-alphanumeric chars & case)."""
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

# 7. Leap Year Checker
def is_leap_year(year: int) -> bool:
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 8. Grading System
def calculate_grade(score: float) -> str:
    """Return letter grade for a numerical score (0-100)."""
    if not (0 <= score <= 100):
        raise ValueError("Score must be between 0 and 100.")
    if score >= 80: return "A"
    if score >= 70: return "B"
    if score >= 60: return "C"
    if score >= 50: return "D"
    return "F"

# 9. Frequency Counter
def count_frequency(items: List) -> Dict:
    """Count occurrence frequencies of elements in a list."""
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq

# 10. Digit Counter
def count_digits(number: int) -> int:
    """Count number of digits in an integer."""
    return len(str(abs(number)))

# 11. Elevator Simulator
def elevator_simulate(current_floor: int, requested_floors: List[int]) -> List[str]:
    """Simulate elevator movement through requested floors."""
    log = []
    floor = current_floor
    for target in requested_floors:
        if target > floor:
            direction = f"Ascending from Floor {floor} to Floor {target} ⬆️"
        elif target < floor:
            direction = f"Descending from Floor {floor} to Floor {target} ⬇️"
        else:
            direction = f"Already at Floor {floor} 🚪"
        log.append(direction)
        floor = target
    return log

# 12. Team Matchup Generator
def team_matchup(teams: List[str]) -> List[Tuple[str, str]]:
    """Pair up teams randomly into matchups."""
    shuffled = teams.copy()
    random.shuffle(shuffled)
    matchups = []
    for i in range(0, len(shuffled) - 1, 2):
        matchups.append((shuffled[i], shuffled[i+1]))
    if len(shuffled) % 2 != 0:
        matchups.append((shuffled[-1], "BYE / Solo"))
    return matchups
