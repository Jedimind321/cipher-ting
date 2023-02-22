#AUTHOR: JEDIMIND321

def txt_to_ASCII(user):
    """
    Func: Converts text to ASCII
    Param: user(str)
    Return: refined_list(list)
    """
    converted_list = [str(ord(char)) for char in user]
    refined_list = []
    for num in converted_list[:]:
        if len(num) <= 2:
            refined_list.append( f'{num:0>3}' )
            continue
        else:
            refined_list.append(num)
    
    return refined_list

    
def ASCII_to_txt(user):
    """
    Func: Converts ASCI to txt
    Param: user(str)
    Return: refined_list(list)
    """
    user = user.split(' ')
    decoded_list = []
    for char in user: 
        decoded_list.append(chr(int(char)))

    return decoded_list



if __name__ == '__main__':
   
    while True:
        choice = input('1 for txt-ASCII \n2 for ASCII-txt\n3 for other options\n>> ')
        if choice == '1':
            user = txt_to_ASCII(input('Enter Text to Convert to ASCII: '))
            print(' '.join(user))
        elif choice == '2':
            user = ASCII_to_txt(input('Enter ASCII to Convert to txt: '))
            print(' '.join(user))
    
        
        elif choice ==  '3':
            while True:
                user2 = input('1 for reversed\n2 for revert to txt\n3 for revert to ASCII\n>> ')
                if user2 == '1':
                    rev_list = list(reversed(user))
                    print(' '.join(rev_list))
                elif user2 == '2':
                     user = ASCII_to_txt(' '.join(user))
                     print(' '.join(user))
                elif user2 == '3':
                    user = txt_to_ASCII(' '.join(user))
                    print(' '.join(user))
                else: 
                    break
        
        else:
            break
