# https://leetcode.com/problems/employee-importance/description/
"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def preProcessEmp(self, employees):
        empMap = {}
        for emp in employees:
            empMap[emp.id] = [emp.importance, emp.subordinates]
        
        return empMap
    
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        empMap = self.preProcessEmp(employees)
        q = []
        root = empMap[id]
        res = 0
        q.append(root)
        while(q):
            node = q.pop()
            res += node[0]
            for child in node[1]:
                q.append(empMap[child])
        return res
