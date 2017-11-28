from action import *
#Latent layer size
N = 49

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

def generate_all_actions(list_actions):
	actions = []
	counter = 1
	actions_set = set()
	for act in list_actions:
		p, pre, eff = generate_action(act[0],act[1])
		a = Action(p, pre, eff)
		if a not in actions_set:
			actions.append(generate_ppdl_action(a.parameters, a.pre_cond, a.effect, 'a'+ str(counter)))
			counter += 1
			actions_set.add(a)
	return actions

def export_pddl(actions, path):
	txt = '(define (domain generated-domain) \n'
  	txt += '    (:requirements :strips) \n'
  	txt += '    (:predicates \n'
  	for i in range(N):
  		txt += '        (p' +str(i) + ' ?v' + str(i) + ') \n'
  	txt += '    )'
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
	print txt
 
#generate_ppdl_action(p,pre,eff,'ac1')

#export_pddl(generate_all_actions([([0,0,1,0,0,1], [1,0,0,0,1,1]), ( [1,0,0,0,1,1], [0,0,1,0,0,1])]), 'domain.pddl')

generate_problem([0,0,1,0,0,1], [1,0,0,0,1,1])
