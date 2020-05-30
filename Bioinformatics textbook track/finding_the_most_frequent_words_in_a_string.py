text=""
k=14

def BA1B(text,k):
    seen = {}
    for i in range(len(text)):
        window = text[i:i+k]
        if window not in seen:
            seen[window] = 1
        else:
            seen[window] +=1 
    highest = max(seen.values())
    return [k for k,v in seen.items() if v == highest]

answer=BA1B(text,k)
print(*answer)
