score= 0
def w():
  print('wrong idiot')
def c():
  print('correct')
player_name = input('what is ur name? ')
print('welcome', player_name)
maths_question= int(input('what is 2^5? '))
if maths_question !=32:
  w()
else:
  c()
  score=score+1
english_question = input('who wrote macbeth? ')
if english_question !='shakespeare':
  w()
else:
  c()
  score=score+1
geo_question= input('what is the capital of pakistan? ')
if geo_question !='islamabad':
  w()
else:
  c()
  score=score+1
question = input('who is the best person in the world? ')
if question !='imran khan':
  w()
else:
  c()
  score=score+1
personal_question = input('what is my favourite colour? ')
if personal_question !='pink':
  w()
else:
  c()
  score=score+1
print(score)