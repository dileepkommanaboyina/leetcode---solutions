class Solution:
    def maximumTime(self, time: str) -> str:
        time = time.split(":")
        # print(time)
        if time[0] == "??":
            time[0] = "23"
        elif time[0][0] == "?":
            if int(time[0][1]) <= 3:
                time[0] = "2" + time[0][1]
            else:
                time[0] = "1" + time[0][1]
        elif time[0][1] == "?":
            if int(time[0][0]) == 2:
                time[0] = time[0][0] + "3"
            else:
                time[0] = time[0][0] + "9"
        if time[1] == "??":
            time[1] = "59"
        elif time[1][0] == "?":
            time[1] = "5" + time[1][1]
        elif time[1][1] == "?":
            time[1] = time[1][0] + "9"
        return ":".join(time)
