from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        un_open_room = set(range(1, len(rooms)))

        def deep(keys: List[int]):
            if not keys:
                return

            for key in keys:
                if key in un_open_room:
                    un_open_room.remove(key)
                    deep(rooms[key])
        deep(rooms[0])
        return not un_open_room


print(Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))