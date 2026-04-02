class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        carList = []
        for i, p in enumerate(position):
            carList.append((p,speed[i]))

        carList.sort(reverse=True)

        stack  = [(target - carList[0][0]) / carList[0][1]]

        for pos, speed in carList:
            time = (target - pos) / speed
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)




        