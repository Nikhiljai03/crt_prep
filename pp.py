# n = 5
# for i in range(n+1):
#     num = 1
#     for j in range(i):
#         print(num, end  = ' ')
#         num += 1
#     print()

# n = 5
# num = 0
# for i in range(n+1):
#     for i in range(i):
#         print(num, end = ' ')
#     num +=1
#     print()

# n = 5
# for i in range(n,0,-1):
#     for j in range(i):
#         print('*' , end =' ')
#     print()

# n = 5
# for i in range(n,0,-1):
#     num = 0
#     for j in range(i):
#         num += 1
#         print(num, end = ' ')
#     print()

# 
# n = 5
# for i in range(1,n+1,1):
#     print(" "*(n-i), end  = "")
#     print("*"*(2*i-1), end = " ")
#     print()
# for i in range(n-1,0,-1):
#     print(" " * (n-i),end = "")
#     print("*" * (2*i-1), end = " ")
#     print( )

# n = 5
# for i in range(n):
#     print("*" * i, end  = ' ')
#     print()
# for j in range(n-1,0,-1):
#     print("*"* j, end  = " ")
#     print()

# n = 5
# for i in range(1,n+1):
#     num = i % 2
#     for j in range(i):
#         print(num, end = ' ')
#         num = 1 - num
#     print()

from langgraph.graph import StateGraph, END

# Define state (like a notebook for data)
class State(dict):
    pass

# Make a new graph
graph = StateGraph(State)

# Create a node (a step in the workflow)
def greet(state):
    state["message"] = "Hello Nikhil! This is LangGraph."
    return state

# Add node to graph
graph.add_node("start", greet)

# Connect node → END
graph.add_edge("start", END)

# Compile graph
app = graph.compile()

# Run graph
result = app.invoke(State())
print(result)
