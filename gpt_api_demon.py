import openai
openai.api_key = "your api key"  #input your personal api_key at here

print('\n')
print("          ------------------------GPT Shell-------------------------\n")
gpt_answer = "\n\nA:"
my_question = "\n\nQ:"

while 1==1:
  enquary = input(my_question)
  #press "quit" to kill the process of the program
  if enquary == 'quit':
    break
  else:
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": enquary }])

  print(gpt_answer,completion['choices'][0]['message']['content'].strip())
