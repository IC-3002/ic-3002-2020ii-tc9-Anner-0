def maximizar(As, D):
    AsSorted=sorted(As, key=lambda tup:tup[1])
    SeqM=[]
    maxTam=0
    i=0
    while i<len(AsSorted):
        if (maxTam + AsSorted[i][1]<=D):
            maxTam=maxTam+AsSorted[i][1]
            SeqM.append(AsSorted[i])
            i+=1
        else:
            break

    return SeqM


# def main():
#     As = [('archivo1', 10), ('archivo2', 5), ('archivo3', 3),
#               ('archivo4', 8), ('archivo5', 9), ('archivo6', 1)]
#     D = 10
#     print(maximizar(As, D))

# main()