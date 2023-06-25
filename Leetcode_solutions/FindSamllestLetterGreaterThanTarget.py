import string

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters = sorted(letters)
        letter = list(string.ascii_lowercase)
        index = 0
        print(letters)
        while index!=len(letters) and letter.index(target)-letter.index(letters[index])>=0:
            index += 1
        if index == len(letters):
            return letters[0]
        return letters[index]