class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

round = Question('Which one?', 'None')

print(round.text)
print(round.answer)