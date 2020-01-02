def locations(short,long):
    results = []

    l = len(short)

    for i in range(len(s) - l):
        if long[i:i+l] == short:
            results.append(i + 1)
    return results

short=""
long=""

print (' '.join(map(str, locations(short, long)))
