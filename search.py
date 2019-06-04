# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
	"""
	This class outlines the structure of a search problem, but doesn't implement
	any of the methods (in object-oriented terminology: an abstract class).

	You do not need to change anything in this class, ever.
	"""

	def getStartState(self):
		"""
		Returns the start state for the search problem.
		"""
		util.raiseNotDefined()

	def isGoalState(self, state):
		"""
		  state: Search state

		Returns True if and only if the state is a valid goal state.
		"""
		util.raiseNotDefined()

	def getSuccessors(self, state):
		"""
		  state: Search state

		For a given state, this should return a list of triples, (successor,
		action, stepCost), where 'successor' is a successor to the current
		state, 'action' is the action required to get there, and 'stepCost' is
		the incremental cost of expanding to that successor.
		"""
		util.raiseNotDefined()

	def getCostOfActions(self, actions):
		"""
		 actions: A list of actions to take

		This method returns the total cost of a particular sequence of actions.
		The sequence must be composed of legal moves.
		"""
		util.raiseNotDefined()


def tinyMazeSearch(problem):
	"""
	Returns a sequence of moves that solves tinyMaze.  For any other maze, the
	sequence of moves will be incorrect, so only use this for tinyMaze.
	"""
	from game import Directions
	s = Directions.SOUTH
	w = Directions.WEST
	return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
	"""
	Search the deepest nodes in the search tree first.

	Your search algorithm needs to return a list of actions that reaches the
	goal. Make sure to implement a graph search algorithm.

	To get started, you might want to try some of these simple commands to
	understand the search problem that is being passed in:

	print("Start:", problem.getStartState())
	print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
	print("Start's successors:", problem.getSuccessors(problem.getStartState()))
	"""
	"*** YOUR CODE HERE ***"
	from util import Stack
	from game import Directions
	fringe = Stack()
	fringe.push(problem.getStartState())
	route=[]
	discovered = []
	routeToCurrent=Stack()
	current = fringe.pop()
	while not problem.isGoalState(current):

		if current not in discovered:

			discovered.append(current)
			successors = problem.getSuccessors(current)

			for new, direction, cost in successors:
				#print(new), print(direction)
				fringe.push(new)
				routeToCurrent.push(route + [direction])

		current = fringe.pop()
		route = routeToCurrent.pop()

	return route

	
	#print("Is the start a goal?", problem.getStartState())
	#print("Start's successors:", problem.getSuccessors(problem.getStartState()))
	#util.raiseNotDefined()

def breadthFirstSearch(problem):
	"""Search the shallowest nodes in the search tree first."""
	"*** YOUR CODE HERE ***"
	from util import Queue
	from game import Directions
	fringe = Queue()
	fringe.push(problem.getStartState())
	route=[]
	discovered = []
	routeToCurrent=Queue()
	current = fringe.pop()
	i = 0
	while not problem.isGoalState(current):
		#print("----iteration ",i," --------, current is : ", current)
		#i+=1
		
		if current not in discovered:
			discovered.append(current)
			successors = problem.getSuccessors(current)

			for new, direction, cost in successors:
				#print("succesor is : ",new," ------")
				fringe.push(new)	
				routeToCurrent.push(route + [direction])


		current = fringe.pop()
		#print(current, " popped----")
		route = routeToCurrent.pop()

	return route

def uniformCostSearch(problem):
	"""Search the node of least total cost first."""
	"*** YOUR CODE HERE ***"
	from util import PriorityQueue
	from game import Directions
	fringe = PriorityQueue()
	fringe.push(problem.getStartState(),0)
	route=[]
	discovered = []
	routeToCurrent=PriorityQueue()
	current = fringe.pop()

	while not problem.isGoalState(current):

		if current not in discovered:

			discovered.append(current)
			successors = problem.getSuccessors(current)

			for new, direction, cost in successors:
				costToCurrent = problem.getCostOfActions(route + [direction])
				fringe.push(new, costToCurrent)	
				routeToCurrent.push(route + [direction],costToCurrent)

		current = fringe.pop()
		route = routeToCurrent.pop()

	return route


def nullHeuristic(state, problem=None):
	"""
	A heuristic function estimates the cost from the current state to the nearest
	goal in the provided SearchProblem.  This heuristic is trivial.
	"""
	return 0

def aStarSearch(problem, heuristic=nullHeuristic):
	"""Search the node that has the lowest combined cost and heuristic first."""
	"*** YOUR CODE HERE ***"
	
	from util import PriorityQueue
	from game import Directions
	fringe = PriorityQueue()
	fringe.push(problem.getStartState(),0)
	route=[]
	discovered = []
	routeToCurrent=PriorityQueue()
	current = fringe.pop()

	while not problem.isGoalState(current):

		if current not in discovered:

			discovered.append(current)
			successors = problem.getSuccessors(current)

			for new, direction, cost in successors:
				costToCurrent = problem.getCostOfActions(route + [direction]) + heuristic(new, problem)
				fringe.push(new, costToCurrent)	
				routeToCurrent.push(route + [direction],costToCurrent)

		current = fringe.pop()
		route = routeToCurrent.pop()

	return route

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
