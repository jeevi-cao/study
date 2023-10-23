
def combine(team=[], result=[], m=1):
    if len(result) == m:
        print(result)
        print("\n")
        return

    for k, v in enumerate(team):
        new_result = result.copy()
        new_result.append(v)
        new_team = team[k+1:]
        combine(new_team, new_result, m)


if __name__ == '__main__':
    team = ["a", "b", "c"]
    combine(team, [], 2)
