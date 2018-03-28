def read_csv_actions(path):
    data = open(path, 'r')
    states = []
    for d in data:
        d = d.split()
        states.append(d)
    return states

path = 'samples/hanoi_real_4_3_49_81_convr/all_states.csv'
actions_list = read_csv_actions(path)
actions_set = set()
for d in actions_list:
	actions_set.add(str(d))
print(len(actions_set))
