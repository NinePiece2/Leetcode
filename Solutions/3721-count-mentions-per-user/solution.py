class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x: (int(x[1]), x[0][2]))
        all_mentions = 0
        result = [0] * numberOfUsers
        online = [0] * numberOfUsers

        for msg_type, time, val in events:
            current = int(time)
            if msg_type[0] == "O":
                online[int(val)] = current + 60
            elif val[0] == "A":
                all_mentions += 1
            elif val[0] == "H":
                for i, t in enumerate(online):
                    if t <= current:
                        result[i] += 1
            else:
                for char in val.split():
                    result[int(char[2:])] += 1
        if all_mentions:
            for i in range(numberOfUsers):
                result[i] += all_mentions
        return result
