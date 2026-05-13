
# Head-Tail-Chance-Calculator

# Coin Flipping Simulator

**This is an educational python project created by an A Level Student interested in Computer Science**

Imagine you have a coin heads and tails.

Imagine you flip that coin 10 times, how many attempts until a 50/50 result? 

Now imagine you flip it 1000 times, again how many tries until after 1000 flips will the number of heads and tails equals?

This program demonstrates and simulates this within the restrictions of a computers "random" bias.

# How to install and run

```bash
git clone https://github.com/Gakaj/Head-Tail-Chance-Calculator.git
```
Navigate to directory, 
```bash
cd Head-Tail-Chance-Calculator.git  
```
## Running the application:

Once in directory simply run:
```bash
python chance-calculator.py
```


## Screenshots and Demo for running in Windows command prompt.
Press for link to ![Demo](HeadTailChanceCalculator/images/) of examplar outputs and inputs.

## How it works:

The roll function:
1. Randomly chooses heads or tails from list
2. If heads add 1 to total_heads, if tails vice versa
3. Iterate this until number of tosses reaches user input
4. If heads = tails, finish and output
5. If not add 1 to attempts and then repeat, recursively calling the function
   - > Issue arises with recurion depth, could alter function to iteration instead of recursively call - time space complextity
6. When head = tail, calculate the average head and tails by totalling and then dividing by attempts
7. Ask user to continue with different amount of tosses, repeat with same or end

##  





