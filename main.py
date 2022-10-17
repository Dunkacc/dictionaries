afc_east_west_wins = {"Bills": 4,
                      "Jets": 3,
                      "Dolphins": 3,
                      "Patriots": 2,
                      "Chiefs": 3,
                      "Fantasy Team":8,
                      "Chargers": 3,
                      "Broncos": 2,
                      "Raiders": 1}
largest_so_far = "Raiders"
for team in afc_east_west_wins.keys():
    if afc_east_west_wins[largest_so_far] < afc_east_west_wins[team]:
        largest_so_far = team
print(f" the team with the most wins is {largest_so_far}\
 with {afc_east_west_wins[largest_so_far]}")