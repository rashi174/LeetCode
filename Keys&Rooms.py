'''
841. Keys and Rooms

There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 
Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.
Initially, all the rooms start locked (except for room 0). 
You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
Example 2:

Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
Note:

1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.


'''

'''
Approach

When visiting a room for the first time, look at all the keys in that room. For any key that hasn't been used yet, 
add it to the todo list (stack) for it to be used.


Algorithm
 
 1. create a stack which will have keys to the room not visited
 2. take a set or list of bools to keep record of rooms seen already.

'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack=[0]  #initially we have key for 0 th room
        seen=[False]*len(rooms) #all rooms are locked
        seen[0]=True #room zero is unlocked
        while stack:
            key=stack.pop()
            for i in rooms[key]:
                if seen[i]==False:
                    seen[i]=True
                    stack.append(i)
        return all(seen) 
