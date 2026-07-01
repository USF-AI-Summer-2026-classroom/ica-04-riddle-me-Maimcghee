from logic import *

# Propositions
    # L = Low level criminals
    # T = tell tale clue
    # H = there is a hole in the ground

    # J = Joker
        # A = Acid
        # C = Cards
        # B = Buzzer

    # R = Riddler
        # Q = Riddler clues 

    # P = Penguin
        # U = Umbrella 

L, T, J, A, C, B, R, Q, P, U, H = vars('L', 'T', 'J', 'A', 'C', 'B', 'R', 'Q', 'P', 'U', 'H')


#knowlage base 

#T
#T > ~L
#T > ( J| R | P)
#R > Q
#P > U
#J > (A | C | B)
# H > (A | U) -> hole in the groud means it could  only be from an umbrella, or acid 
   

# Formulas
f01 = T
f02 = ( J| R | P) >> T #  All super villans leave clues but clues are NOT exclusive to super villans 
f03 = R >> Q
f04 = P >> U
f05 = J >> (A | C | B)
f06 = H
f07 = H >> ( U | A)


# ArgumentForms

low_level = ArgumentForm(f01,f02,f03,f04, f05, f06,f07,conclusion = L)
joker = ArgumentForm(f01,f02,f03,f04, f05, f06,f07, conclusion = J)
penguin = ArgumentForm(f01,f02,f03,f04, f05, f06,f07, conclusion = P)
riddler = ArgumentForm(f01,f02,f03,f04, f05, f06,f07, conclusion = R)
print('Who definitely commited this crime: ')
print('A low-level criminal: ', low_level.is_valid())
print('The Joker committed this crime: ', joker.is_valid())
print('The Penguin: ', penguin.is_valid())
print('The Riddler: ', riddler.is_valid())


