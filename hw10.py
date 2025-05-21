import os
import pickle

filename = "score.bin"

def input_scores(scrs):
    i = 1
    print('[점수 입력]')

    while True:
        score = int(input(f'#{i}? '))
        if score < 0:
            return scrs
        scores.append(score)
        i += 1

def get_average(avr):
    sum_scores = 0
    for j in range(len(avr)):
        sum_scores += avr[j]
    average = sum_scores / len(avr)
    return average

def show_scores(scrs):
    print('\n[점수 출력]')
    print(f'개인점수: ', end='')

    for k in scrs:
        print(k, end=' ')

    print(f'\n평균: {get_average(scrs):.1f}')

def save_scores(scrs, filepath):
    with open(filepath, 'wb') as file:
        pickle.dump(scrs, file)

def load_scores(filepath):
    with open(filepath, 'rb') as file:
        scores = pickle.load(file)
        return scores


if os.path.exists(filename):
    scores = load_scores(filename)

    print('[파일 읽기]')
    show_scores(scores)

else:
    scores= []
    inputed_scores = input_scores(scores)
    show_scores(inputed_scores)
    save_scores(inputed_scores, filename)
