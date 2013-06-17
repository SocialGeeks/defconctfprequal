## OMGACM 3  
OMGACM: 3 points  
grandprix  
stay away from the zebras.  
grandprix.shallweplayaga.me:2038  

#### I was right on the money, just need to become a better python coder & CS major...
      http://raz0r.name/other/defcon-ctf-2013-quals-grandprix-writeup/

##### likely need to use a https://en.wikipedia.org/wiki/A*_search_algorithm such as: http://stackoverflow.com/questions/4159331/python-speed-up-an-a-star-pathfinding-algorithm
###### Driving game (looks like fun!)
      nc grandprix.shallweplayaga.me 2038
      Use 'l' and 'r' to move. Don't crash.
      Press return to start
      
      |-----|
      |     |
      |     |
      |     |
      |     |
      |     |
      |     |
      |     |
      |     |
      |  u  |
      |-----|
      l
      |-----|
      |     |
      |     |
      |     |
      |     |
      |     |
      |     |
      |     |
      |     |
      | u   |
      |-----|
      r
      |-----|
      | P   |
      |     |
      |     |
      |     |
      |     |
      |     |
      |     |
      |     |
      |  u  |
      |-----|
      
###### Solution plan
      pseudo code
            1. intake road map into python graph
            2. load graph into pathing algo
            3. determine and send next move (l,r,\n)
            4. capture return data
                  4a. data appears to be another road grid
                        4a1. Yes - goto 1
                        4a2. No dump data to screen.
      example grid:
             0123456
             |-----|
            0|  r  |
            1| c   |
            2|     |
            3|   ~ |
            4| Z   |
            5|  ~  |
            6|     |
            7|     |
            8|Z u  |
            9|-----|

      basic algo found from pyhton docs:
            graph =     {
                        '00': ['01', '10'],
                        '01': ['00', '02', '11'],
                        '03': ['04', '13'],
                        '04': ['03', '14'],
                        '10': ['00', '20'],
                        '12': ['13', '22']
                        }
            
            def find_shortest_path(graph, start, end, path=[]):
                  path = path + [start]
                  if start == end:
                  return path
                  if not graph.has_key(start):
                  return None
                  shortest = None
                  for node in graph[start]:
                  if node not in path:
                      newpath = find_shortest_path(graph, node, end, path)
                      if newpath:
                          if not shortest or len(newpath) < len(shortest):
                              shortest = newpath
                  return shortest
            
            print find_shortest_path(graph, 'A', 'D') 
