#Code to generate a pddl using variables
#Deprecated
def generate_ppdl_action_old(parameter, pre_cond, effect, action_name):
	action = '(:action ' + str(action_name) + '\n'
	action += '    :parameters ('
	for par in range(len(parameter)):
		if abs(parameter[par]): action+= '?v' + str(par) + ' '
	action += ')'+ '\n'
	action += '    :precondition (and' + '\n'
	for pre in range(len(pre_cond)):
		if pre_cond[pre] == 1:  action+='        ('+ 'p' + str(pre) + ' ?v'+ str(pre) + ')' +'\n'
		if pre_cond[pre] == -1:  action+='        (not ('+ 'p' + str(pre) + ' ?v'+ str(pre) + '))' +'\n'
	action  += '    )' +'\n'
	action += '    :effect(and' + '\n'
	for eff in range(len(effect)):
		if not effect[eff]: continue
		if effect[eff] == 1: action += '        ('+ 'p' + str(eff) + ' ?v'+ str(eff) + ')' +'\n'
		if effect[eff] == -1: action += '        (not ('+ 'p' + str(eff) + ' ?v'+ str(eff) + '))' +'\n'
	action += '    )' +'\n'
	action += ')\n'
	return action

#Deprecated
def export_pddl_old(actions, path):
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

#Deprecated
def generate_problem_old(init_state, goal_state):
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