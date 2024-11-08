import classes

def objective_function(cents_adjustments):

    #create notes
    A = classes.Note("A", 0)
    B = classes.Note("B", 200 + cents_adjustments[0])
    C = classes.Note("C", 300+ cents_adjustments[1])
    D = classes.Note("D", 500+ cents_adjustments[2])
    E = classes.Note("E", 700+ cents_adjustments[3])
    F_sharp = classes.Note("F_sharp", 900+ cents_adjustments[4])
    G = classes.Note("G", 1000+ cents_adjustments[5])

    intervals = []

    AtoC = classes.Interval(A, C, 315.641)
    AtoE = classes.Interval(A, E, 701.955)
    EtoG = classes.Interval(E, G, 315.641)
    EtoB = classes.Interval(E, B, 701.955)
    GtoB = classes.Interval(G, B, 386.314)
    GtoD = classes.Interval(G, D, 701.955)
    DtoFsharp = classes.Interval(D, F_sharp, 386.314)
    DtoAoctave = classes.Interval(D, A, 701.955)


    intervals.append(AtoC)
    intervals.append(AtoE)
    intervals.append(EtoG)
    intervals.append(EtoB)
    intervals.append(GtoB)
    intervals.append(GtoD)
    intervals.append(DtoFsharp)
    intervals.append(DtoAoctave)

    output = 0
    for interval in intervals:
        output+= (interval.interval_in_cents - interval.just_cents_diff) ** 2
        #print(interval.interval_in_cents,interval.just_cents_diff)

    #print(output)
    return output