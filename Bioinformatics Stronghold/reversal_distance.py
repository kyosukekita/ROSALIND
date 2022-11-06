#勉強資料https://scholarworks.sjsu.edu/cgi/viewcontent.cgi?referer=&httpsredir=1&article=1103&context=etd_projects

#解法１
def best_intersection(P, Q):
  for perm in P:
    if perm in Q:
      return P[perm] + Q[perm]
  return -1

def make_step(processed, border, next_border):
  for perm in border:
    for j in range(len(perm)+1):
      for i in range(j-1): # at least 2 numbers reversed
        new_perm = perm[:i] + perm[i:j][::-1] + perm[j:]  # reverse [i,j]

        if new_perm not in processed and new_perm not in border:
          next_border[new_perm] = border[perm] + 1

  processed.update(border)
  border.clear()
  border.update(next_border)
  next_border.clear()

def rev_dist(perm1, perm2):
  processed1 = {}
  border1 = {}
  next_border1 = {}

  processed2 = {}
  border2 = {}
  next_border2 = {}

  border1[tuple(perm1)] = 0
  border2[tuple(perm2)] = 0

  lamp = False
  while best_intersection(border1, border2) == -1:
    if lamp:
      make_step(processed1, border1, next_border1)
    else:
      make_step(processed2, border2, next_border2)
    lamp = not lamp

  return best_intersection(border1, border2)





#別解
import sys
from collections import deque

def all_permtuations(P):
    for i in range(len(P)):
        for j in range(i + 2, len(P) + 1):
            yield P[:i] + P[i:j][::-1] + P[j:]


def reversal_distance(p1, p2):
    if p1 == p2:
        return 0

    target = tuple(p2)
    fromfirst = {tuple(p1): 0}
    q = deque((p1, ))
    while len(q):
        s = q.popleft()
        c = fromfirst[s]
        for j in all_permtuations(s):
            if j == target:
                return c + 1
            if j not in fromfirst:
                fromfirst[j] = c + 1
                if c != 4:
                    q.append(j)
    fromsecond = {tuple(p2): 0}
    target = tuple(p1)
    q = deque((p2, ))
    answer = 1e5
    while len(q):
        s = q.popleft()
        c = fromsecond[s]
        if c == 4:
            break
        for j in all_permtuations(s):
            if j == target:
                return c + 1
            if j not in fromsecond:
                fromsecond[j] = c + 1
                if c != 3:
                    q.append(j)
            if j in fromfirst:
                answer = min(answer, fromfirst[j] + fromsecond[j])
    return answer


if __name__ == "__main__":
    '''
    Given: A collection of at most 5 pairs of permutations, all of which have length 10.
    Return: The reversal distance between each permutation pair.
    '''
    input_lines = sys.stdin.read().splitlines()
    all_dist = []
    for idx in range(0, len(input_lines), 3):
        P1 = tuple(map(int, input_lines[idx].split()))
        P2 = tuple(map(int, input_lines[idx + 1].split()))

        dist = reversal_distance(P1, P2)
        all_dist.append(dist)

    print(' '.join(map(str, all_dist)))
