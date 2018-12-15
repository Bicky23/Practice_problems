from random import choice

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert","gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjs = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
preps = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
advs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]
vowels = ["a", "e", "i", "o", "u"]

def make_poem():
    noun1, noun2, noun3 = choice(nouns), choice(nouns), choice(nouns)
    verb1, verb2, verb3 = choice(verbs), choice(verbs), choice(verbs)
    adj1, adj2, adj3 = choice(adjs), choice(adjs), choice(adjs)
    prep1, prep2 = choice(preps), choice(preps)
    adv1 = choice(advs)
    first_word = choice(["A", "An"]) 
    if first_word == "A":
        while adj1[0] in vowels:
            adj1 = choice(adjs)
    else:
        while adj1[0] not in vowels:
            adj1 = choice(adjs)
    sent =  first_word + " " + adj1 + " " + noun1 + " " + verb1 + " " + prep1 + " the " + adj2 +  " " + noun2 + " " + adv1 + ", the " + noun1 + " " + verb2 + " the " + noun2 + " " + verb3 + " " + prep2 + " " +  "a" + " " + adj3 + " " + noun3  
    return sent

print(make_poem())




