def stableMatching(menPreferences,womenPreferences):
  numPeople = len(menPreferences)
  menEngaged = [-1] * numPeople
  womenEngaged = [-1] * numPeople
  menProposals = [0] * numPeople
  while -1 in menEngaged:
    for man in range(numPeople):
      if menEngaged[man] == -1:
        woman = menPreferences[man][menProposals[man]]
        menProposals[man] += 1
        if womenEngaged[woman] == -1:
          womenEngaged[woman] = man
          menEngaged[man] = woman
        else:
          currentPartner = womenEngaged[woman]
          if womenPreferences[woman].index(man)<womenPreferences[woman].index(currentPartner):
            womenEngaged[woman] = man
            menEngaged[man] = woman
            menEngaged[currentPartner] = -1

  marriages = [(man,woman) for man,woman in enumerate(menEngaged)]
  print("Stable Marriages are : ")
  print(marriages)

menPreferences = [
    [0,1,2],
    [1,0,2],
    [0,1,2]
]

womenPreferences = [
    [0,1,2],
    [1,2,0],
    [2,1,0]
]


stableMatching(menPreferences,womenPreferences)