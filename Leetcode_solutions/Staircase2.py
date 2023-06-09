def staircaspb2(w,h):
    minh=h[0]
    largindex=0
    for i in range(len(h)):
        if min>h[i]:
            min=h[i]
            largmin=i
    ans=0
    for j in range(min):
            ans+=j
    elmtpris=[min]
    avant_dernier=0
    dernier=0
    while len(elmtpris)!=len(h):
        min2=100000
        if largmin!=1:
            for o in range(1,largmin):
                ans+=o
        for i in range(len(h)):
            if min2>h[i] and h[i] not in elmtpris:
                min2=h[i]
                largmin=w[i]
        elmtpris.append(min2)
        dernier+=1 
        for k in range(elmtpris[avant_dernier],elmtpris[dernier]):
            ans+=k
        avant_dernier+=1
    return ans