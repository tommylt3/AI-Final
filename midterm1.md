# Midterm 1 Study Guide

## Chapter 3
A problem consists of five parts: **the initial state**, **a set of actions**,
**a transition model describing the results of those actions**, **a set of
goal states**, and an action cost function.

### Search Strategies
   1. Completeness: Does it always finde a solution, if one exists
   2. Time Complexity: Number of Nodes
   3. Space Complexitiy: Max Number Of Nodes In Memory
   4. Optimality: Does it Always Find at least one solution
   
- Time and Space Complexity are always measured in terms
  - b: Maximum branching factor of Nodes
  - d: Depth of the least costed Solution
  - m: maximum depth of the state space
  
### Uninformed Search Strategies

#### Trees

Uninformed search methods have access only to the problem
definition. Algorithms build a search tree in an attempt to find a
solution

  1. Breadth-first search
      1. Completeness: Yes, if b is finite
      2. Time Complexity: O(b^d+1)
      3. Space Complexitiy: O(b^d+1) 
      4. Optimality: Yes, if action costs are identical
      5. Critical Error: Space is the largest problem
  2. Uniform-cost search
      1. Completeness: Yes, if b is finite and/or has a solution
      2. Time Complexity: O(b^fC*/cl), C∗ is the cost of the optimal solution
      3. Space Complexitiy: O(b^fC*+cl) 
      4. Optimality: Yes (if cost = 1 per step); not generally optimal
  3. Depth-first search
      1. Completeness: No, incomplete when m is non-finite. Complete in finite spaces
      2. Time Complexity: O(b^m)
      3. Space Complexitiy: O(bm) 
      4. Optimality: No
  4. Depth-limited search
      1. Completeness: No 
      2. Time Complexity: O(b^l)
      3. Space Complexitiy: O(bl) 
      4. Optimality: No
  5. Iterative deepening search
      1. Completeness: Yes, if b is finite
      2. Time Complexity: O(b^d)
      3. Space Complexitiy: O(bd) 
      4. Optimality: Yes, if action costs are identical

### Informed Search Strategies
Informed search methods have access to a heuristic function
h(n) that estimates the cost of a solution from n.


#### Graphs
  1. Greedy Search 
    1. Completeness: No, gets stuck in loops
    2. Time Complexity: O(b^m), but good heuristics give dramatic improvements
    3. Space Complexitiy: O(bd^m)
    4. Optimality: No
  2.  A* Search 
      1. Completeness: Yes, unless there are infiniteley many nodes with f <= f(G)  
      2. Time Complexity: Exponential in [relative error h * lendth of solutio(n)]
      3. Space Complexitiy: Keeps all nodes in memory
      4. Optimality: Yes
- Evaluation Function f(n) = g(n) +h(n) 
    h(n) = cost so far to reach n
    g(n) = estimated cost to goal from n
    f(n) = estimated total path from n to goal

## Chapter 4
  1. Local search methods keep only a small number of states in memory that are useful for optimization.
  2. In nondeterministic environments, agents can apply AND–OR search to generate contingency plans that reach the goal regardless of which outcomes occur during execution.
  3. Belief-state is the set of possible states that the agent is in for partially observable environments.
  4. Standard search algorithms can be applied directly to belief-state space to solve sensorless problems.

## Chapter 5

### Game Theory
- Two Players, both making optimal moves with fully observable moves (ie. the opponent knows your full move)
- Moves: Make Action
- Position: Game State
- Zero Sum Game
  - W/L Game
  - No Win-Win Outcome

| Information Level       | Chance                             | Deterministic                     |
|-------------------------|------------------------------------|-----------------------------------|
| Perfect Information      | backgammon, monopoly               | chess, checkers, go, othello     |
| Imperfect Information    | battleship, blind tic tac toe      | bridge, poker, scrabble, nuclear war |


### Optimal Descisions in Games

#### Min-Max
- Each Player takes turns choosing what the best solution for them will be
- The algorithm calculates to a depth of d, the best solution assuming the opponent will also make the best descision.
       
1. Completeness: Yes, if tree is finite
2. Time Complexity: O(b^m)
3. Space Complexitiy: O(bm), exact solution isnt feasible for large branching factors such as chess
4. Optimality: Yes, against an optimal opponent

##### Alpha Beta Pruning
- Alpha : Is the best value (to max), found for the current branch
- Beta: Is the worst value (to max), found for the current branch
**Pruning does not effect final descision result**, rather it just eliminates pathes that would never contribute solutions to the min-max search space.
- **Time Complexity Becomes: O(b^m/2)** 
  1. Doubles Solvable Depth
  

##### Monte Carlo 
- Monte Carlo does not use a heuristic to decide games, rather it simulates X number of games and back propagates wins to figure out the best possible move. 
- Still uses min-max assuming opponent is doing the same simulations calculation. 

## Chapter 6 

### Defining CSPs
A constraint satisfaction problem has 3 key components
1. **X** is a set of variables, ```x = set()```
2. **D** is a set of domains, ```d = {domain for domain in x: {}}```
3. **C** is a set of constraints that specify allowable cominations of values.

CSPS deal with assingment of values to variables
- Complete Assignment is when every variable is assigned a value and a solution to a CSP is constent to all constraints.
- Partial Assignment is when some variables are left unassigned.

#### Types of Constraints

Unary constraints involve a single variable,
- SA != green
Binary constraints involve pairs of variables,
- SA != WA
Higher-order constraints involve 3 or more variables,
- cryptarithmetic column constraints
Preferences (soft constraints)
- red is better than green, often representable by a cost for each variable assignment
  1. constrained optimization problems


### Standard Search  Formulation of CSP's

```
function Backtracking-Search(csp) returns solution/failure
    return Recursive-Bac k t r a cking({ }, csp)
function Recursive-Backtracking(assignment, csp) returns soln/failure
    if assignment is complete then return assignment
    var ← Select-Unassigned-Variable(Variables[csp], assignment, csp)
    for each value in Order-Domain-Values(var, assignment, csp) do
        if value is consistent with assignment given Constraints[csp] then
            add {var = value} to assignment
            result ← Recursive-Bac k t r a cking(assignment, csp)
            if result /= failure then return result
            remove {var = value} from assignment
    return failure
```

**Initial State** = Empty Assignment
**Successor Function** = Assign a Value to an Unassigned Variable that does not conflict with current assignment, Fails If No Legal Assignments
**Goal Test** = The Current Assignment Is Complete

1. This is the same for all CPSs
2. Every Solution Appears at depth N, where N is the number of variables
   1. Uses DFS (fastest solution)
3. Path is irrelvant, so can also use complete-state formulation 

**Only need too consider assignments to a single variable at each node**
```{NT = Green, WA = Red} == {NT = Red, WA = Green}```
DFS search for all single-variable assignments is called backtracking search
Backtracking search is the basic uninformed algorithm for CSPs

#### Improvements for CSPS

##### Forward Checking
##### 