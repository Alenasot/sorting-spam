# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 16:53:58 2022

@author: Елена Еремеева
"""
#4.На почту приходят сообщения, которые необходимо отсортировать (желательные и нежелательные)

    
with open ('письмо.txt', encoding='utf-8') as letter:
    text_letter = letter.read().split('\n')
    #print(text_letter)
    lenght = 0
    for item in text_letter:
        lenght += len(item)
    #print(lenght)
    if lenght <= 200:
        print('Письмо помещено в раздел нежелательной почты')
    elif lenght > 200:
        count = 1
        for item in text_letter: 
            if '#' in item:
                print('Письмо помещено в раздел нежелательной почты')
                break
            elif '@' in item:
                print('Письмо помещено в раздел нежелательной почты')
                break
            elif 'дорогой' in item.lower() and 'друг' in item.lower():
                print('Письмо помещено в раздел нежелательной почты')
                break
            elif 'всем' in item.lower() and 'приветик' in item.lower():
                print('Письмо помещено в раздел нежелательной почты')
                break
            elif 'ваша' in item.lower() and 'подписка' in item.lower():
                print('Письмо помещено в раздел нежелательной почты')
                break 
            else: 
                count += 1
                if count == len(text_letter):
                    print('Получено новое письмо')