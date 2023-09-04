import random

def get_message(message: str):
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there! '
    
    if message == 'roll':
        return str(random.randint(1, 6))
    
    if p_message == '!help':
        return "This is the messege that you can modify. "