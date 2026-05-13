import random



run = "Y"

tosses = 0
attempts = 1



    
def rollWA(tosses, attempts, average_head, average_tail):
  
  headTail = ("Head", "Tail")
  head = 0
  tail = 0
  result = []
  for i in range(0, tosses):
    result.append(random.choice(headTail))
    toss = random.choice(['head', 'tail'])

    if toss== "head": 
      head = head + 1 
    elif toss== "tail": 
      tail = tail + 1
    #print (head, tail)
    
    i+=1
    if i == tosses:
      
      #print(results) 
      print("Number of heads: " + str(head), "Number of tails: " + str(tail))
      average_head.append(head)
      average_tail.append(tail)
      

      if head != tail:

        attempts += 1 #if not a match add 1 to attempts
        rollWA(tosses, attempts, average_head, average_tail) #run function again

      else:
        print("It took the program ", attempts, "attempts to get a 50/50 result!")
        #calculate average
        average_num_head = round(sum(average_head) / attempts)
        average_num_tail = round(sum(average_tail)/ attempts)  
        print(f"Averagely there was {average_num_head} heads and {average_num_tail} tails.")
        run = input("Would you like to restart the program, for same number of throws, type R (Y/N/R)")
        start(run,tosses,rollWA, attempts)
        
      
      

################################################################################################################################
def start(run, tosses, rollWA, attempts):
  average_head = []
  average_tail = []
  if run == "Y":
    attempts = 1
    tosses = int(input("Input number of coin tosses: "))
    rollWA(tosses, attempts, average_head, average_tail)
  elif run == "N":
    print("--Program Ended--")
  elif run == "R":
    attempts = 1
    rollWA(tosses, attempts, average_head, average_tail)
  else:
    print(ValueError("Input Incorrect"))
    
if run != "":
  start(run, tosses, rollWA, attempts)