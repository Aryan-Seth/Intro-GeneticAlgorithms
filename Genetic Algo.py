from re import I
from numpy.random import randint
from numpy.random import rand

n_pop = 50
bitsize = 20


def onemax(x):
    score = []
    for i in range(n_pop):
        score.append(sum(x[i]))

    return score


def popinit(n_pop, bitsize):
    pop = [randint(0, 2, bitsize).tolist() for _ in range(n_pop)]
    return pop

# pop=popinit(n_pop,bitsize)


def selection(pop, scores, k=2):

    selection_ix = randint(len(pop))
    for ix in randint(0, len(pop), k-1):

        if scores[ix] < scores[selection_ix]:
            selection_ix = ix
    return pop[selection_ix]


def crossover(fit):
    x = len(fit)
    #r_mut = 0.9
    for i in range(n_pop-1):
      t = randint(1, 18)
      c1=fit[i];c2=fit[i+1]
      for i in range(0, x-1):
          pop = c1[:t]+c2[t:]
    return pop


def mutation(pop, r_mut):
    x = 50
    c1=pop;
    for i in range(0, x):
        if rand() < r_mut:
            t = randint(0, 19)
            c1[t] = 1-c1[t]
    return pop


def main():
    pop = popinit(n_pop, bitsize)
    scores = onemax(pop)
    print(scores)
    best = 0
    best_eval = scores[0]
    for gen in range(100):
        for i in range(n_pop):
            if scores[i] > best_eval:
                best, best_eval = pop[i], scores[i]
        print(">%d, new best f(%s) = %.3f" % (gen,  best, best_eval))

        selected = [selection(pop, scores) for _ in range(n_pop)]
        pop = crossover(selected)
        pop = mutation(pop, 0.5)
    return[best, best_eval]


print("let's go?")
for i in range(0, 10):
   a= main()
   print(a[0]," ",a[1])
