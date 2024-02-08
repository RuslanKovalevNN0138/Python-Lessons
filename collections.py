import collections

l1=[1,1,1,2,2,3,4]
# counter - dict for counting values
count=collections.Counter(l1)

# deq - double ended queue
deq=collections.deque(l1)
deq.append(5)
deq.appendleft(3)
a=deq.pop()
b=deq.popleft()

# default dict - dict with default value
default_dict_list=collections.defaultdict(list)
default_dict_set=collections.defaultdict(set)

# chain map
d1={0:1, 2:3}
d2={4:5, 6:7}
ch_map=collections.ChainMap(d1,d2)

if __name__=="__main__":
    
    # print counter
    print(count.most_common(2))
    # print deque
    print(deq)
    print(a)
    print(b)
    # print default dict
    default_dict_list[1].append(3)
    default_dict_set[2].add(4)

    print(default_dict_list)
    print(default_dict_set)
    # print chain map
    print(ch_map[2])
