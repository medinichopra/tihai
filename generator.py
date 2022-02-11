import random

tihai = [] #full set of three with the gaps
palla = [] #individual set of beats
bol = [2, 3, 5, 7]

def structure():
    #finds number of beats per turn and corresponding gap
    taal = int(input("Enter your taal: ")) #number of beats in the taal
    avartan = int(input("Enter your avartan: ")) #number of times to repeat the taal
 
    total = avartan*taal + 1
    return(divmod(total, 3)) #calculates division of beats and gaps

def generate(t):
    #generates a possible combination of beats for the individual set
    if(t == 1 or t == 2 or t == 3 or t == 5):
        palla.append(t)
        return
    if(t == 4):
        palla.extend((2, 2))
        return

    i = 0
    r = 3
    found = False
#need to add condition for if equal to t
#assumption: a 'good' tihai has pairs of beats like 2-2 or 3-3 instead of one off patterns - i.e. symmetry
#unless its an outlier at the end^
    while(found == False):
        i = random.randint(0, r)
        if(bol[i]*2 < t):
            found = True
            palla.extend((bol[i], bol[i]))
            generate(t-2*bol[i])
        else:
            r = i

def main():
    ekhai, gap = structure()
    generate(ekhai)

    #different types based on bol type, does mapping to bol, just experimenting 
    replacements = {2:'tigdadigdig tigdadigdig', 3:'takitdhikit takitdhikit', 5:'taktakit taktakit taktakit taktakit', 7:'taktaktakit taktaktakit taktaktakit taktaktakit'}
    bol_tihai = replacements.get
    print([bol_tihai(n, n) for n in palla])

    #creates the tihai with individual set calculated above + gaps
    if(gap == 0):
        tihai.extend((palla, palla, palla))
    else:
        tihai.extend((palla, gap/2, palla, gap/2, palla))
    print("Tihai:", tihai)

main()
