from action import *
#Latent layer size
N = 36



#============ LOGIC OPERATORS ==============
def _or(self,other):
        return [se | so for se,so in zip(self,other)]   

def _xor(self,other):
        return [se ^ so for se,so in zip(self,other)]

#A special xnor that returns -1 if both are 0
def _xnor(self, other):
	return [sxnor(se,so) for se,so in zip(self,other)]

def sxnor(se,so):
	if (se == 0) and (so == 0):
		return -1
	if (se == 1) and (so == 1):
		return 1
	if (se == -1) and (so == -1):
		return -1
	return 0 

#===========================================
#============ ACTION MANAGEMENT ============
def generate_action(state1, state2):
	parameter = _or(state1,state2) 
	pre_cond = _xnor(state1,state1)
	xor = _xor(state1,state2)
	effect = [0] * len(state1)
	for i in range(len(xor)):
		if not xor[i]: continue
		if ((state1[i] == 1) and (xor[i] == 1)): 
			effect[i] = -1
		else: 
			effect[i] = 1 
	return parameter, pre_cond, effect



def generate_ppdl_action(parameter, pre_cond, effect, action_name):
	action = '(:action ' + str(action_name) + '\n'
	action += '    :parameters ()\n'
	action += '    :precondition (and' + '\n'
	for pre in range(len(pre_cond)):
		if pre_cond[pre] == 1:  action+='        ('+ 'p' + str(pre) +')' +'\n'
		if pre_cond[pre] == -1:  action+='        (not ('+ 'p' + str(pre) +'))' +'\n'
	action  += '    )' +'\n'
	action += '    :effect(and' + '\n'
	for eff in range(len(effect)):
		if not effect[eff]: continue
		if effect[eff] == 1: action += '        ('+ 'p' + str(eff) + ')' +'\n'
		if effect[eff] == -1: action += '        (not ('+ 'p' + str(eff) + '))' +'\n'
	action += '    )' +'\n'
	action += ')\n'
	return action


def generate_all_actions_pddl(list_actions):
	actions = []
	counter = 1
	for a in list_actions:
		actions.append(generate_ppdl_action(a.parameters, a.pre_cond, a.effect, 'a'+ str(counter)))
		counter += 1
	return actions


def generate_all_actions(list_actions):
	actions = []
	counter = 1
	actions_set = set()
	for act in list_actions:
		p, pre, eff = generate_action(act[0],act[1])
		a = Action(p, pre, eff)
		actions_set.add(a)
	return actions_set

#===========================================
#============ PDDL OUTPUT ==================

def export_pddl(actions, path):
	txt = '(define (domain generated-domain) \n'
  	txt += '    (:requirements :strips :negative-preconditions) \n'
  	txt += '    (:predicates \n'
  	for i in range(N):
  		txt += '        (p' +str(i) + ') \n'
  	txt += '    )\n'
  	for action in actions:
  		txt += action
  	txt += ')'
	data = open(path, 'wb')
	data.write(txt)



def generate_problem(init_state, goal_state):
	txt = '(define (problem pb1)\n'
 	txt += '    (:domain generated-domain)\n'
   	txt += '    (:requirements :strips :negative-preconditions)\n'
  	txt += '    (:init\n'
	for pre in range(len(init_state)):
		if init_state[pre]:  txt+='       ('+ 'p' + str(pre) + ')' +'\n'
		else: txt+='       (not ('+ 'p' + str(pre) + '))' +'\n'
	txt += '    )\n'
	txt += '    (:goal\n'
	txt += '      (and\n'
	for pre in range(len(goal_state)):
		if goal_state[pre]:  txt+='       ('+ 'p' + str(pre) + ')' +'\n'
		else: txt+='       (not ('+ 'p' + str(pre) + '))' +'\n'
	txt += '      )\n'
	txt += '    )\n)'
	return txt


def read_csv_actions(path):
	data = open(path, 'r')
	actions = []
	for d in data:
		d = d.split()
		line = [int(i) for i in d]
		s1 = line[:len(line)/2]
		s2 = line[len(line)/2:]
		actions.append((s1,s2))
	return actions

#===========================================
#========= PRUNING AND EXECUTION ===========

def prune_actions(actions):
	meta_actions = []
	effect_dict = dict()
	for a in actions:
		k = str(a.effect)
		if k in effect_dict:
			effect_dict[k].append(a)
		else:
			effect_dict[k] = [a]
	actions_set = set()
	cont = 0
	for key in effect_dict.keys():
		acts = effect_dict[key]
		new_pre_cond = acts[0].pre_cond
		for a in acts:
			cont += 1
			new_pre_cond = _xnor(new_pre_cond,a.pre_cond)
		new_action = Action(_or(map(abs, new_pre_cond),acts[0].effect), new_pre_cond, acts[0].effect)
		actions_set.add(new_action)
	print len(effect_dict.keys())
	print len(actions_set)
	print 'xors' , cont
	return actions_set

def check_match(act, pre_cond):
	for a,b in zip(act,pre_cond):
		if (b == 0):
			continue
		if (a == 0) and (b ==-1):
			continue
		if (a == 1) and (b == 1):
			continue
		return False
	return True 

def check_action(actions, state_1, state_2):
	action_list = []
	p, pre, eff = generate_action(state_1, state_2)
	print pre
	for a in actions:
		if check_match(state_1, a.pre_cond):
			action_list.append(a)
	print len(action_list)
	for a in action_list:
		if a.effect == eff:
			print 'Found', a.effect

#===========================================
#============ MODULES AND MAIN =============

def create_domain():
	transitions = read_csv_actions('samples/puzzle_mnist_3_3_36_20000_conv/all_actions.csv')
	actions = generate_all_actions(transitions)
	print len(actions)
	pruned = prune_actions(actions)
	pdll_actions = generate_all_actions_pddl(pruned)
	export_pddl(pdll_actions, 'new_domain.pddl')



def create_problem():
	transitions = read_csv_actions('samples/puzzle_mnist_3_3_36_20000_conv/all_actions.csv')
	actions = generate_all_actions(transitions)
	print len(actions)
	pruned = prune_actions(actions)
	check_action(pruned,transitions[0][0], transitions[0][1])
	print transitions[0][0]
	print _xnor(transitions[0][0], transitions[0][1])
	problem = generate_problem(transitions[0][0], transitions[0][1])
	#0 1 1 1 0 0 1 0 1 0 1 0 0 0 1 1 0 1 1 0 0 1 1 0 1 1 0 1 0 1 0 0 1 1 1 1 1 1 1 0 0 1 1 0 1 0 1 0 1 0 1 1 0 1 1 0 0 1 1 0 1 1 0 1 0 1 0 0 1 1 1 1
	print len(transitions[0][0]), len(transitions[0][1])
	data = open('new_problem.pddl', 'wb')
	data.write(problem)
	p, pre, eff = generate_action(transitions[0][0], transitions[0][1])
	print eff
create_problem()
