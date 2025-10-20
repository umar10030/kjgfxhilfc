class IntegerToRoman:
    def __init__(self):
        # Mapping of Roman numerals
        self.value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def convert(self, num):
        roman_numeral = ''
        for value, symbol in self.value_map:
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral

if __name__ == "__main__":
    converter = IntegerToRoman()
    try:
        while True:
            s = input("Enter a positive integer (or 'q' to quit): ").strip()
            if not s or s.lower() in ('q', 'quit', 'exit'):
                print("Goodbye.")
                break
            try:
                number = int(s)
            except ValueError:
                print("Invalid input — please enter an integer.")
                continue
            if number <= 0:
                print("Please enter a positive integer.")
                continue
            # Note: classical Roman numerals typically cover up to 3999,
            # but this converter will produce repeated 'M' for larger values.
            roman = converter.convert(number)
            print(f"{number} in Roman numerals is: {roman}\n")
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")