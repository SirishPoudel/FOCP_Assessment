import sys


class League:
    def __init__(self, team, Win=0, Lose=0, Draw=0, For=0, Against=0, Difference=0, Points=0, Played=0) -> None:
        self.w = Win
        self.l = Lose
        self.d = Draw
        self.f = For
        self.a = Against
        self.diff = Difference
        self.pts = Points
        self.p = Played
        self.team = team

    def score_calc(self, For, Against):
        """ For calculation of the point table. """

        self.f += For
        self.a += Against
        self.p += 1
        self.diff += (For - Against)
        if For > Against:
            self.w += 1
            self.pts += 3
        elif For < Against:
            self.l += 1
        else:
            self.d += 1

def read_file(file_name):  
    """ Read the files. """

    with open(file_name,"r") as file:
        return file.read().split("\n")

def table(team):
    """ Prints table. """

    # Takes the user input from the command line, if given.
    user_input = sys.argv[1:]
    if user_input:
        for user in user_input:
            print(user.rjust(25))
        # Simply for the design
        print("\n" + "*"*50 + "\n")
    # For the table content
    print(f"P W D L  F   A  Diff Pts".rjust(35))
    for i in team:
        print(f"{i.team:10} {i.p} {i.w} {i.d} {i.l} {i.f:3} {i.a:3} {i.diff:4} {i.pts:>3}")

def main():
    """ This is the main function. """

    team = []
    teams = read_file("team.csv")
    results = read_file("result.csv")
    for t in teams:
        obj =  League(t)
        team.append(obj)
    # For extracting points from the csv file
    for i in results:   
        for j in team:
            abc=i.split(",")
            if j.team == abc[0]:
                j.score_calc(int(abc[1]),int(abc[3]))

            elif j.team == abc[2]:
                j.score_calc(int(abc[3]),int(abc[1]))
          
    team.sort(reverse=True, key=lambda val: (val.pts, val.diff))
    table(team)

main()