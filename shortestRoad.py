#!/usr/bin/python3
# coding=utf-8
import itertools
import random

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et sett med hardkodete
# instanser som kan ses lengre nedre, og muligheten for å generere
# tilfeldige instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved å justere på verdiene under.

# Kontrollerer om det genereres tilfeldige instanser.
generate_random_tests = False
# Antall tilfeldige tester som genereres.
random_tests = 10
# Laveste mulige antall rader og kolonner i generert instans.
n_lower = 3
# Høyest mulig antall rader og kolonner i generert instans.
# NB: Om dette antallet settes høyt vil det ta veldig lang tid å kjøre
# testene, da mulige svar sjekkes ved bruteforce.
n_upper = 5
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0


from collections import deque

def shortest_road(build_map, start, end):

    q_S_to_E = deque([start])
    q_E_to_S = deque([end])

    width = len(build_map)
    if width == 0:
        return None
    
    height = len(build_map[0])
    if height == 0:
        return None


    kanter = [(1,0),(0,-1),(-1,0),(0,1)]
    parent_S_to_E = {start:None}
    parent_E_to_S = {end:None}

    while q_S_to_E and q_E_to_S:

        # START TO END PART
        u_S_to_E = q_S_to_E.popleft()
        if u_S_to_E == end:
            path = []
            current = end

            while current is not None:
                
                path.append(current)
                current = parent_S_to_E[current]

            path.reverse()
            return path
            
        for kant in kanter:
            nextNode= (u_S_to_E[0]+kant[0],u_S_to_E[1]+kant[1])
            if -1 < nextNode[0] < width and -1 < nextNode[1] < height:


                if build_map[nextNode[0]][nextNode[1]] and nextNode not in parent_S_to_E:

                    parent_S_to_E[nextNode] = u_S_to_E

                    q_S_to_E.append(nextNode)    
                                            
                    ##### CHECK IF FOUND IN BACKWARDS SEARCH
                    if nextNode in parent_E_to_S:
                        

                        path = []
                        current = nextNode

                        # CONSTRUCT PATH FOR FIRST HALF
                        while current is not None: 
                            path.append(current)
                            current = parent_S_to_E[current]
                        
                        path.reverse()

                        # CONSTUCT FOR SECOND HALF

                        current = parent_E_to_S[nextNode]
                        while current is not None:
                            path.append(current)
                            current = parent_E_to_S[current]

                        return path

                        



        # END TO START PART
        u_E_to_S = q_E_to_S.popleft()
        if u_E_to_S == start:
            path = []
            current = start

            while current is not None:
                
                path.append(current)
                current = parent_E_to_S[current]

            path.reverse()
            return path
            
        for kant in kanter:
            nextNode= (u_E_to_S[0]+kant[0],u_E_to_S[1]+kant[1])
            if -1 < nextNode[0] < width and -1 < nextNode[1] < height:

                if build_map[nextNode[0]][nextNode[1]] and nextNode not in parent_E_to_S:
                    parent_E_to_S[nextNode] = u_E_to_S

                    q_E_to_S.append(nextNode)        

                    ##### CHECK IF FOUND IN FORWARDS SEARCH
                    if nextNode in parent_S_to_E:
                        
                        path = []
                        current = nextNode

                        # CONSTRUCT PATH FOR FIRST HALF
                        while current is not None: 
                            path.append(current)
                            current = parent_S_to_E[current]
                        
                        path.reverse()

                        # CONSTUCT FOR SECOND HALF

                        current = parent_E_to_S[nextNode]
                        while current is not None:
                            path.append(current)
                            current = parent_E_to_S[current]

                        return path
                    

    return None


# from collections import deque

# def shortest_road(build_map, start, end):

   

#     width = len(build_map)
#     if width == 0:
#         return None

#     height = len(build_map[0])
#     if height == 0:
#         return None

#     q = deque([start])
#     kanter = [(1,0),(0,-1),(-1,0),(0,1)]
#     # parent = {start:None}
#     parent = [[None] * height for _ in range(width)]
#     parent[start[0]][start[1]] = start

#     while q:
#         u = q.popleft()
#         if u == end:
#             path = []
#             current = end

#             while current != start:
                
#                 path.append(current)
#                 current = parent[current[0]][current[1]]

#             path.append(start)
#             path.reverse()
#             return path
            
#         for kant in kanter:
#             nextNode= (u[0]+kant[0],u[1]+kant[1])
#             if -1 < nextNode[0] < width and -1 < nextNode[1] < height:
#                 if build_map[nextNode[0]][nextNode[1]] and parent[nextNode[0]][nextNode[1]] == None:   #nextNode not in parent:

#                         parent[nextNode[0]][nextNode[1]] = u

#                         q.append(nextNode)

#     return None


# from collections import deque

# def shortest_road(build_map, start, end):

#     q = deque([start])


#     kanter = [(1,0),(0,-1),(-1,0),(0,1)]
#     parent = {start:None}

#     while q:
#         u = q.popleft()
#         if u == end:
#             path = []
#             current = end

#             while current is not None:
                
#                 path.append(current)
#                 current = parent[current]

#             path.reverse()
#             return path
            
#         for kant in kanter:
#             nextNode= (u[0]+kant[0],u[1]+kant[1])
#             try:
#                 if build_map[nextNode[0]][nextNode[1]] and nextNode not in parent:
#                     # build_map[nextNode[0]][nextNode[1]] = "VISITED" 

#                     parent[nextNode] = u

#                     q.append(nextNode)
#             except:
#                 pass
#     return None




# Disjoint-set forest
class Set:
    def __init__(self):
        self.__p = self
        self.rank = 0

    @property
    def p(self):
        if self.__p != self:
            self.__p = self.__p.p
        return self.__p

    @p.setter
    def p(self, value):
        self.__p = value.p


def union(x, y):
    x = x.p
    y = y.p
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        y.rank += x.rank == y.rank


# Hardkodete tester på format: (build_map, start, end), lengde på korteste vei
tests = [
    (([[True, True]], (0, 1), (0, 0)), 2),
    (([[True, False, True]], (0, 0), (0, 2)), None),
    (([[True, True, True]], (0, 0), (0, 2)), 3),
    (([[True, True, False]], (0, 1), (0, 0)), 2),
    (([[True], [True]], (1, 0), (0, 0)), 2),
    (([[True, False], [True, True]], (0, 0), (1, 1)), 3),
    (([[False, True], [True, True]], (0, 1), (1, 0)), 3),
    (([[True, True], [True, True]], (1, 1), (0, 0)), 3),
    (([[False, False, True], [True, False, True]], (1, 2), (0, 2)), 2),
    (([[False, False], [True, True], [False, False]], (1, 1), (1, 0)), 2),
    (([[True, False], [True, False]], (0, 0), (1, 0)), 2),
    (([[True, False], [False, False], [True, True]], (0, 0), (2, 1)), None),
    (([[False, False, True], [False, False, True], [True, False, True]], (0, 2), (2, 2)), 3),
    (([[False, False], [True, True], [False, False]], (1, 1), (1, 0)), 2),
    (([[True, True, True], [False, False, False]], (0, 2), (0, 1)), 2),
    (([[True, False, True], [True, False, False]], (0, 2), (1, 0)), None),
    (([[True, True], [False, False], [False, True]], (0, 0), (0, 1)), 2),
    (([[False, True, False], [False, True, False]], (1, 1), (0, 1)), 2),
]


# Treg bruteforce løsning
def bruteforce_solve(build_map, start, end):
    coordinates = set((x, y) for x in range(len(build_map))
                             for y in range(len(build_map[0]))
                             if build_map[x][y]
                      )
    coordinates -= {start, end}
    if verify_answer_internal(build_map, start, end, [start, end]) is None:
        return 2
    for k in range(1, len(coordinates) + 1):
        if any(verify_answer_internal(build_map, start, end,
                                      [start] + list(perm) + [end]) is None
               for perm in itertools.permutations(coordinates, r=k)):
            return k + 2
    return None


def verify_answer_internal(build_map, start, end, student):
    for pos in student:
        if not (
            0 <= pos[0] < len(build_map)
            and 0 <= pos[1] < len(build_map[0])
        ):
            return "Du prøver å bygge utenfor kartet."
        if not build_map[pos[0]][pos[1]]:
            return "Du prøver å bygge en plass der det ikke er mulig å bygge."
    else:
        disjoint_set = {pos: Set() for pos in student}
        for pos in student:
            for i, j in [
                (pos[0] + 1, pos[1]),
                (pos[0] - 1, pos[1]),
                (pos[0], pos[1] + 1),
                (pos[0], pos[1] - 1),
            ]:
                if (i, j) in disjoint_set and disjoint_set[
                    (i, j)
                ].p != disjoint_set[pos].p:
                    union(disjoint_set[pos], disjoint_set[(i, j)])
        if start not in disjoint_set:
            return "Du har ikke med startlandsbyen i listen."
        if end not in disjoint_set:
            return "Du har ikke med sluttlandsbyen i listen."
        if disjoint_set[start].p != disjoint_set[end].p:
            return "Listen din gir ikke en sammenhengende vei."


def verify_answer(build_map, start, end, student, answer):
    if answer is None and student is not None:
        return "Du returnerte en liste med posisjoner når riktig svar var None."
    if student is None and answer is not None:
        return "Du returnerte None, selv om det finnes en løsning."
    if student is not None and answer < len(student):
        return "Det finnes en liste med færre koordinater som fortsatt danner en gyldig vei."
    if student is not None:
        return verify_answer_internal(build_map, start, end, student)


def gen_examples(nl, nu, k):
    for _ in range(k):
        prob = random.randint(0, 10)/10
        rows = random.randint(min(nl, 2), nu)
        columns = random.randint(min(nl, 1), nu)
        start = (random.randint(0, rows - 1), random.randint(0, columns - 1))
        end = start
        while end == start:
            end = (random.randint(0, rows - 1), random.randint(0, columns - 1))
        build_map = [
            [random.random() < prob for _ in range(columns)]
            for _ in range(rows)
        ]
        build_map[start[0]][start[1]] = True
        build_map[end[0]][end[1]] = True
        yield (build_map, start, end), bruteforce_solve(build_map, start, end)


if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(n_lower, n_upper, random_tests))

failed = False
for test_case, answer in tests:
    build_map, start, end = test_case
    student_map = [i[:] for i in build_map]
    student = shortest_road(student_map, start, end)
    response = verify_answer(build_map, start, end, student, answer)
    if response is not None:
        if failed:
            print("-"*50)
        failed = True
        map_string = "#" * (2 + len(build_map[0])) + "\n#" + \
                      "#\n#".join("".join([" ", "X"][not x] for x in row) for row in build_map) + \
                      "#\n" + "#" * (2 + len(build_map[0]))
        print(f"""
Koden feilet for følgende instans.
build_map: ({build_map})
{map_string}

start: {start}
end: {end}

Feilmelding: {response}
Ditt svar: {student}
        """)

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")
