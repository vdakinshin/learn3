answers = {
    'привет': 'И тебе привет!', 
    'как дела': 'Лучше всех!', 
    'пока': 'Увидимся'
}

def get_answer(question,answers):
	return answers.get(question,'скажи мне что-нибудь другое...')

def ask_user():
    while True:
        try:
            user_answer = input('Что скажешь?: ')
            user_answer = str.lower(user_answer)
            replay_to_user = get_answer(user_answer,answers)
            print(replay_to_user)
        except KeyboardInterrupt:
            print('Ну зачем ты так?!')
            break
        if user_answer == 'пока':
            break

if __name__ == '__main__':
    ask_user()
