class StringUtility:
    def __init__(self, string):
        self.string = string
    def __str__(self):
        string = self.string
        return string
    def vowels(self):
        string = self.string
        vowels = "aeiou"
        count = 0
        for i in string:
            if i in vowels:
                count+=1
        if count < 5:
            string = str(count)
        else:
            string = "many"
        return string
    def bothEnds(self):
        string = self.string
        if len(string) > 2:
            string = string[0] + string[1] + string [-2] + string[-1]
        else:
            string = ""
        return string
    def fixStart(self):
        string = self.string
        if len(string) > 1:
            parameter = string[0]
            test = string[1:]
            new = ""
            for i in test:
                if i == parameter:
                    i = "*"
                new+=i
            string = parameter + new
        return string
    def asciiSum(self):
        total = 0
        for i in self.string:
            total += ord(i)
        return total
    def cipher(self):
        shift = len(self.string)
        result = ""
        for char in self.string:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                new_pos = (ord(char) - start + shift) % 26
                char = chr(start + new_pos)
            result += char
        return result
