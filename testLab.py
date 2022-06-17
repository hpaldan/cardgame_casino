



pCards = [12]
fCards = [12,2,3,4]
moveList = []

"""Function that is supposed to get all card combinations from a hand."""
def getCombinations(fCards):

    def recFunc(q,resVec,Q):
        if len(resVec) > 0:
            for j in range(len(resVec)):
                q_temp = q.copy()
                q_temp.append(resVec[j])
                Q.append(q_temp)
                print(f'All values: j:{j}, q:{q}, q_temp: {q_temp}, Q: {Q}, resVec[j+1:-1]: {resVec[j+1:len(resVec)]}')
                recFunc(q_temp,resVec[j+1:len(resVec)],Q)
        else:
            print('Finished')

    fCardsSize = len(fCards)
    #fCards.sort(reverse=True)
    Q = [[el] for el in fCards]
    for i in range(fCardsSize):
        q = [fCards[i]]
        resVec = fCards[i+1:fCardsSize]

        recFunc(q,resVec,Q)

    print(f'final Q: {Q}')
    print(fCardsSize)
    print(len(Q))

def main():

    getCombinations(fCards)


if __name__ == "__main__":
    main()





