# Roman to Int

class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        mapping_table = {
            "IV": "4",
            "IX": "9",
            "XL": "40",
            "XC": "90",
            "CD": "400",
            "CM": "900"
        }
        result = 0

        replaced = True
        while replaced:
            replaced = False
            for key, value in mapping_table.items():
                if key in s:
                    s = s.replace(key, value, 1)  # Replace only the first occurrence
                    result += int(mapping_table.get(key))
                    replaced = True

        print(s)

        s = [*s]
        for letter in s:
            for key in romanDict:
                if letter == key:
                    result += romanDict.get(letter)
        return result
        # print(result)        Testing local


# Testing local
# solution_instance = Solution()

# solution_instance.romanToInt("LVIII")