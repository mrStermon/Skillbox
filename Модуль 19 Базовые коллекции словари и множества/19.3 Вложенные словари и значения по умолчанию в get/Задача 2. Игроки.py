players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

team_a_members = [
    player['name']
    for player in players_dict.values()
    if player.get('team') == 'A' and player.get('status') == 'Rest'
]
team_b_members = [
    player['name']
    for player in players_dict.values()
    if player.get('team') == 'B' and player.get('status') == 'Training'
]
team_c_members = [
    player['name']
    for player in players_dict.values()
    if player.get('team') == 'C' and player.get('status') == 'Travel'
]
print(team_a_members)
print(team_b_members)
print(team_c_members)
