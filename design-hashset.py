class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.data.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.data.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.data

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

def testCase(commandList,commandParams):
    res = []
    for i in range(len(commandList)):
        if commandList[i]=='MyHashSet':
            obj = MyHashSet()
            res.append(None)
        elif commandList[i]=='add':
            obj.add(commandParams[i][0])
            res.append(None)
        elif commandList[i]=='contains':
            res.append(obj.contains(commandParams[i][0]))
        elif commandList[i]=='remove':
            res.append(obj.remove(commandParams[i][0]))
        else:
            print('command not found!!!')
    print(res)

testCase(["MyHashSet","add","add","contains","contains","add","contains","remove","contains"],
    [[],[1],[2],[1],[3],[2],[2],[2],[2]])