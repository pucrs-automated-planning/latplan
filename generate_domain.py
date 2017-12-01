from action import *
#Latent layer size
N = 36

def generate_action(state1, state2):
	parameter = _or(state1,state2) 
	pre_cond = state1
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
	action += '    :parameters ('
	for par in range(len(parameter)):
		if parameter[par]: action+= '?v' + str(par) + ' '
	action += ')'+ '\n'
	action += '    :precondition (and' + '\n'
	for pre in range(len(pre_cond)):
		if pre_cond[pre]:  action+='        ('+ 'p' + str(pre) + ' ?v'+ str(pre) + ')' +'\n'
	action  += '    )' +'\n'
	action += '    :effect(and' + '\n'
	for eff in range(len(effect)):
		if not effect[eff]: continue
		if effect[eff] == 1: action += '        ('+ 'p' + str(eff) + ' ?v'+ str(eff) + ')' +'\n'
		if effect[eff] == -1: action += '        (not ('+ 'p' + str(eff) + ' ?v'+ str(eff) + '))' +'\n'
	action += '    )' +'\n'
	action += ')\n'
	return action

def _or(self,other):
        return [se | so for se,so in zip(self,other)]   

def _xor(self,other):
        return [se ^ so for se,so in zip(self,other)]

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


def export_pddl(actions, path):
	txt = '(define (domain generated-domain) \n'
  	txt += '    (:requirements :strips) \n'
  	txt += '    (:predicates \n'
  	for i in range(N):
  		txt += '        (p' +str(i) + ' ?v' + str(i) + ') \n'
  	txt += '    )\n'
  	for action in actions:
  		txt += action
  	txt += ')'
	data = open(path, 'wb')
	data.write(txt)

def generate_problem(init_state, goal_state):
	txt = '(define (problem pb1)\n'
 	txt += '    (:domain generated-domain)\n'
   	txt += '    (:requirements :strips :negative-preconditions)'
  	txt += '    (:objects'
  	for i in range(N):
  		txt += '        o' + str(i) + '\n'
  	txt += '    )\n'
	txt += '    (:init\n'
	for pre in range(len(init_state)):
		if init_state[pre]:  txt+='       ('+ 'p' + str(pre) + ' o'+ str(pre) + ')' +'\n'
		else: txt+='       (not ('+ 'p' + str(pre) + ' o'+ str(pre) + '))' +'\n'
	txt += '    )\n'
	txt += '    (:goal\n'
	txt += '      (and\n'
	for pre in range(len(goal_state)):
		if goal_state[pre]:  txt+='       ('+ 'p' + str(pre) + ' o'+ str(pre) + ')' +'\n'
		else: txt+='       (not ('+ 'p' + str(pre) + ' o'+ str(pre) + '))' +'\n'
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
	for key in effect_dict.keys():
		acts = effect_dict[key]
		new_pre_cond = [0] * len(acts[0].pre_cond)
		for a in acts:
			new_pre_cond = _xor(new_pre_cond,a.pre_cond)
		new_action = Action(acts[0].parameters, new_pre_cond, acts[0].effect)
		actions_set.add(new_action)
	print len(effect_dict.keys())
	print len(actions_set)
	return actions_set

#generate_ppdl_action(p,pre,eff,'ac1')

#export_pddl(generate_all_actions([([0,0,1,0,0,1], [1,0,0,0,1,1]), ( [1,0,0,0,1,1], [0,0,1,0,0,1])]), 'domain.pddl')
transitions = read_csv_actions('samples/puzzle_mnist_3_3_36_20000_conv/all_actions.csv')
actions = generate_all_actions(transitions)
print len(actions)
pruned = prune_actions(actions)
pdll_actions = generate_all_actions_pddl(pruned)
export_pddl(pdll_actions, 'new_domain.pddl')
generate_problem([0,0,1,0,0,1], [1,0,0,0,1,1])
