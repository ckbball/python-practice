class Quiz:
  def __init__(self):
    self.qs = ["What's 9+10?", "How many 2's make a fish?", "Cash me outside"]
    self.ans = [21, 2, "How bow duh"]
    self.q1 = "What's 9+10?"
    self.a1 = 21
    self.q2 = "How many 2's make a fish?"
    self.a2 = 2
    self.q3 = "Cash me outside"
    self.a3 = "How bow duh"

  def checkAnswer(self, questionNum, answer):
    if questionNum == 1:
      answer = int(answer)
      if answer == self.a1:
        return 1
      else:
        return 0
    elif questionNum == 2:
      answer = int(answer)
      if answer == self.a2:
        return 1
      else:
        return 0
    elif questionNum == 3:
      if answer == self.a3:
        return 1
      else: 
        return 0
    else:
      return 0


q1 = Quiz()

chances = 2
ques = 1

for x in range(4):
  if chances == 0:
    print("Ah you are out of chances. Nice try, better luck next time")
    break
  question = q1.qs[ques-1]
  txt = raw_input(question)
  check = q1.checkAnswer(ques, txt)
  if check == 1:
    print("Aha you got that question right. On to the next one!")
    ques += 1
  else:
    chances -= 1
    ques += 1
    txt1 = "Darn you didn't answer that one right. But don't worry you still have {} chances left to answer {} questions correctly."
    print(txt1.format(chances, ques))
  if ques > 3:
    break

print("Thanks for trying out our quiz game. See you next time!")


