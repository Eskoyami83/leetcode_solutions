from heapq import heapify, heappush, heappop

def mostBooked(self, n, meetings):
        r = [0] * n
        ts = 0
        avail = range(n)
        heapify(avail)
        used = [] # (free ts, room id)
        for start, stop in sorted(meetings):
            if ts < start:
                ts = start
            while used and used[0][0] <= start:
                _, i = heappop(used)
                heappush(avail, i)
            if not avail:
                ts, i = heappop(used)
                heappush(avail, i)
            i = heappop(avail)
            r[i] += 1
            heappush(used, (ts + stop - start, i))
        _, r = min((-v, i) for i, v in enumerate(r))
        return r