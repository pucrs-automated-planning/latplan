#!/usr/bin/env python3

from action import *
from subprocess import call
from os import listdir
from os.path import isfile, join
import os, errno
import ast
import random
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from encode_decode import EncoderDecoder
from latplan.util.plot import *
import numpy as np
#Latent layer size
#N = 36
FD_PATH = '../fast_downward/'
MP_PATH = '../MauPlanner/'
SIZE_H = 42
SIZE_W = 42
ONLINE_REQ_JAR = ''

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

def _act(se,so):
    if so != -1: return se | so
    else: return 0

def exec_action(state,eff):
    return [_act(se,so) for se,so in zip(state,eff)]

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

def export_pddl(actions, path, N):
    txt = '(define (domain generated-domain) \n'
    txt += '    (:requirements :strips :negative-preconditions) \n'
    txt += '    (:predicates \n'
    for i in range(N):
      txt += '        (p' +str(i) + ') \n'
    txt += '    )\n'
    for action in actions:
      txt += action
    txt += ')'
    data = open(path, 'w')
    data.write(txt)



def generate_problem(init_state, goal_state):
    txt = '(define (problem pb1)\n'
    txt += '    (:domain generated-domain)\n'
#    txt += '    (:requirements :strips :negative-preconditions)\n'
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

def generate_problem_no_negatives(init_state, goal_state):
    txt = '(define (problem pb1)\n'
    txt += '    (:domain generated-domain)\n'
#    txt += '    (:requirements :strips :negative-preconditions)\n'
    txt += '    (:init\n'
    for pre in range(len(init_state)):
        if init_state[pre]:  txt+='       ('+ 'p' + str(pre) + ')' +'\n'
        #else: txt+='       (not ('+ 'p' + str(pre) + '))' +'\n'
    txt += '    )\n'
    txt += '    (:goal\n'
    txt += '      (and\n'
    for pre in range(len(goal_state)):
        if goal_state[pre]:  txt+='       ('+ 'p' + str(pre) + ')' +'\n'
        else: txt+='       (not ('+ 'p' + str(pre) + '))' +'\n'
    txt += '      )\n'
    txt += '    )\n)'
    return txt


def export_problem_pgr(init_state,path=''):
    txt = '(define (problem pb1)\n'
    txt += '    (:domain generated-domain)\n'
#    txt += '    (:requirements :strips :negative-preconditions)\n'
    txt += '    (:init\n'
    for pre in range(len(init_state)):
        if init_state[pre]:  txt+='       ('+ 'p' + str(pre) + ')' +'\n'
#        else: txt+='       (not ('+ 'p' + str(pre) + '))' +'\n'
    txt += '    )\n'
    txt += '    (:goal\n'
    txt += '      (and\n'
    txt += '            <HYPOTHESIS>\n'
    txt += '      )\n'
    txt += '    )\n)'
    data = open(path+'template.pddl', 'w')
    data.write(txt)


def read_csv_actions(path):
    data = open(path, 'r')
    actions = []
    for d in data:
        d = d.split()
        line = [int(i) for i in d]
        s1 = line[:int(len(line)/2)]
        s2 = line[int(len(line)/2):]
        actions.append((s1,s2))
    return actions

def export_actions(actions,path='pddl_actions.csv'):
    data = open(path, 'w')
    counter = 1
    for a in actions:
        rep = 'a'+ str(counter) + '@' + str(a.pre_cond) + '@' + str(a.effect) + '\n'
        data.write(rep)
        counter += 1

def read_pddl_actions(path='pddl_actions.csv'):
    data = open(path, 'r')
    list_actions = []
    for d in data:
        split = d.split("@")
        pred = ast.literal_eval(split[1])
        eff = ast.literal_eval(split[2].split('\n')[0])
        a = Action([], pred,eff)
        a.name = split[0]
        list_actions.append(a)
    return list_actions

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
    #print pre
    for a in actions:
        if check_match(state_1, a.pre_cond):
            action_list.append(a)
    for a in action_list:
        if a.effect == eff:
            #print 'Found', a.effect
            return a

#===========================================
#============== PGR EXPORTS ================

def export_trace_obs(trace, path='obs.dat'):
    data = open(path, 'w')
    for action in trace:
        data.write(action + '\n')

def export_hypothesis(list_goals, path='hyps.dat'):
    data = open(path, 'w')
    first = True
    for state in list_goals:
        txt = ''
        for pre in range(len(state)):
            if not first: txt+= ','
            if state[pre]:  txt+='('+ 'p' + str(pre) + ')'
            else: txt+='(not ('+ 'p' + str(pre) + '))'
            first = False
        data.write(txt + '\n')
        first = True
        
        


#===========================================
#=========== HELPERS FOR MODULES ===========

def create_domain(actions_path, path, exp_actions='pddl_actions.csv'):
    transitions = read_csv_actions(actions_path)
    actions = generate_all_actions(transitions)
    #print( len(actions))
    pruned = prune_actions(actions)
    pddl_actions = generate_all_actions_pddl(pruned)
    export_pddl(pddl_actions, path, N)
    export_actions(pruned,exp_actions)
    return len(transitions), len(actions),len(pruned)


def generate_DFS_problem(actions, state, steps=5):
    action_list = []
    current_state = state
    for x in range(steps):    
        for a in actions:
            if check_match(current_state, a.pre_cond):
                action_list.append(a.name)
                current_state = exec_action(current_state, a.effect)
                break
    return current_state, action_list

def create_problem(init, goal, path='new_problem.pddl'):
    problem = generate_problem(init, goal)
    data = open(path, 'w')
    data.write(problem)

def create_problem_no_negatives(init, goal, path='new_problem.pddl'):
    problem = generate_problem_no_negatives(init, goal)
    data = open(path, 'w')
    data.write(problem)


def create_problem_DFS(init, actions='pddl_actions.csv', path='problem.pddl'):
    actions =  read_pddl_actions(actions)
    goal, a_list = generate_DFS_problem(actions,init)
    problem = generate_problem(init, goal)
    data = open(path, 'w')
    data.write(problem)
    #print a_list

def convert_traces_to_transitions(init,trace,pddl_actions='pddl_actions.csv'):
    actions = read_pddl_actions(pddl_actions)
    current_state = init
    transitions = [init]
    for t in trace:
        for a in actions:
            if a.name == t:
                current_state = exec_action(current_state, a.effect)
                break;
        transitions.append(current_state)
    return transitions

#Converts traces to transicitions using FD sas_plan
def cvt_ttotran_FD(init,pddl_actions='pddl_actions.csv',path='sas_plan'):
    raw_trace = open(path, 'r')
    trace = []
    for line in raw_trace:
        if ';' in line:
            break
        trace.append(line.split()[0].replace('(', '').replace(')', ''))
    transitions = convert_traces_to_transitions(init, trace, pddl_actions)
    return transitions

def cvt_ttotran_MP(init,pddl_actions='pddl_actions.csv',path='sas_plan'):
    raw_trace = open(path, 'r')
    trace = []
    for line in raw_trace:
        if 'Planning' in line:
            continue
        trace.append(line.split()[0].replace('(', '').replace(')', '').replace("    ", ""))
    transitions = convert_traces_to_transitions(init, trace, pddl_actions)
    return transitions


def cvt_trantotrace(transitions,actions='pddl_actions.csv'):
    tuples = []
    for x in range(len(transitions)-1):
        tuples.append((transitions[x], transitions[x + 1]))
    actions = read_pddl_actions(actions)    
    list_actions = []
    for t in tuples:
        a = check_action(actions, t[0], t[1])
        list_actions.append(a.name)
    return list_actions

#create_domain()
#print read_pddl_actions()[-1], read_pddl_actions()[-1].name
#export_trace_obs(cvt_trantotrace(cvt_ttotran_FD()))
#list_hyp = [[0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]]
#export_hypothesis(list_hyp)
#export_hypothesis([goal], path='real_hyp.dat')

def plan_fd(path_domain, path_problem):
    #print FD_PATH+'fast_downward.py'
    call([FD_PATH+'fast-downward.py', path_domain, path_problem, '--search' ,'astar(lmcut())'])

def plan_mp(path_domain, path_problem):
    f = open("sas_plan", "w")
    call(['ruby', MP_PATH+'MauPlanner.rb', path_domain, path_problem, '-a', 'blindc'], stdout=f)

def percentage_slice(_list, per):
    new_size = int(math.ceil(len(_list) * per))
    if new_size == 0: 
        new_size = 1
    copy = list(_list)
    while len(copy) > new_size:
        index = random.randrange(len(copy))
        copy.pop(index)
    return copy

def save_plan_img(transitions, path, sae, SIZE_H, SIZE_W):
    list_images = []
    for t in transitions:
        list_images.append(sae.decode(t, False))
    plot_grid_m(np.array(list_images),10,path, SIZE_H, SIZE_W)


def plot_grid_m(images,w=10,path="plan.png", SIZE_H=42, SIZE_W=42, verbose=False):
    l = 0
    #images = fix_images(images)
    l = len(images)
    h = int(math.ceil(l/w))
    plt.figure(figsize=(w*1.5, h*1.5))
    for i,image in enumerate(images):
        ax = plt.subplot(h,w,i+1)
        try:
            plt.imshow(image.reshape(SIZE_H,SIZE_W),interpolation='nearest',cmap='gray')
        except TypeError:
            TypeError("Invalid dimensions for image data: image={}".format(np.array(image).shape))
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    print(path) if verbose else None
    plt.tight_layout()
    plt.savefig(path)
    plt.close()



#===========================================
#============ MODULES AND MAIN =============

def setup_complete_test(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    create_domain('samples/puzzle_mnist_3_3_36_20000_conv/all_actions.csv', path+'/domain.pddl')
    init = [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1]
    list_hyp = [[0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],[0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1]]
    goal = [0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1]
    create_problem(init, goal, path + '/problem.pddl')
    plan_fd(path+'/domain.pddl', path+'/problem.pddl')
    export_problem_pgr(init, path+ '/')
    export_trace_obs(cvt_trantotrace(cvt_ttotran_FD(init)), path + '/obs.dat')
    export_hypothesis(list_hyp, path=path + '/' + 'hyps.dat')
    export_hypothesis([goal], path=path+ '/' +'real_hyp.dat')

def module_create_domain(actions, domain, output_dir):
    import timeit
    output_path = output_dir+domain+'_domain.pddl'
    exp_actions = output_dir+domain+'_actions.csv'
    data = open(output_dir+domain+'_logs.txt', 'w')
    data.write('Creating domain from: '+ actions + ' to: '+ output_path + '\n')
    data.write('PDDL_CSV:' + exp_actions + '\n')
    start_time = timeit.default_timer()
    transitions_len, actions_len, pruned_len = create_domain(actions, output_path, exp_actions)
    elapsed = timeit.default_timer() - start_time
    data.write('Total transitions: '+ str(transitions_len)+ '\n')
    data.write('Distinct transitions: '+ str(actions_len)+ '\n')
    data.write('Actions generated: '+ str(pruned_len)+ '\n')
    data.write('Time elapsed: '+ str(elapsed)+ '\n')


def set_up_pgr(network_folder,path_domain, path_dir, path_output='out1', pddl_actions='pddl_actions.csv', obs=100, plan=False):
    print("Working on:", path_domain, path_dir)
    enc_dec = EncoderDecoder(network_folder)
    onlyfiles = [f for f in listdir(path_dir) if isfile(join(path_dir, f))]
    img_init = enc_dec._open_image(path_dir+'/init.png')
    SIZE_H, SIZE_W = img_init.shape     
    init = enc_dec.encode(path_dir+'/init.png', True)
    goal = enc_dec.encode(path_dir+'/goal.png', True)
    candidate_goals = []
    for f in onlyfiles:
        if 'c' in f:
            candidate_goals.append(enc_dec.encode(path_dir+'/'+f, True))

    try:
        os.makedirs(path_output)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    create_problem(init, goal, path_output + '/problem_neg.pddl')
    create_problem_no_negatives(init, goal, path_output + '/problem.pddl')
    if plan:
        print("Planning: ", path_domain, path_dir)
        plan_mp(path_domain, path_output+'/problem.pddl')
        print("Done")
    else:
        print("Planning skiped!")
    save_plan_img(cvt_ttotran_MP(init.tolist(),pddl_actions), path_output + '/plan.png', enc_dec, SIZE_H, SIZE_W)
    export_problem_pgr(init, path_output+ '/')
    transitions = cvt_ttotran_MP(init,pddl_actions)
    traces = cvt_trantotrace(cvt_ttotran_MP(init,pddl_actions),pddl_actions)
    p_traces = percentage_slice(traces, float(obs)/100.0)
    call(['cp', path_domain, path_output+ '/' +'domain.pddl'])
    call(['cp', 'sas_plan', path_output+ '/' +'log.txt'])
    export_trace_obs(p_traces, path_output + '/obs.dat')
    #transitions[0] = transitions[0].tolist()
    #print(transitions)
    export_hypothesis(transitions, path_output + '/obs2.dat')
    export_hypothesis(candidate_goals, path=path_output + '/' + 'hyps.dat')
    export_hypothesis([goal], path=path_output+ '/' +'real_hyp.dat')

#setup_complete_test('mnist01')
#plan_fd('new_domain.pddl','new_problem.pddl')

def set_up_online_pgr(network_folder,path_domain, path_dir, path_output='out1', pddl_actions='pddl_actions.csv', obs=100, plan=False):
    print("Working on:", path_domain, path_dir)
    enc_dec = EncoderDecoder(network_folder)
    onlyfiles = [f for f in listdir(path_dir) if isfile(join(path_dir, f))]
    img_init = enc_dec._open_image(path_dir+'/init.png')
    SIZE_H, SIZE_W = img_init.shape     
    init = enc_dec.encode(path_dir+'/init.png', True)
    goal = enc_dec.encode(path_dir+'/goal.png', True)
    candidate_goals = []
    for f in onlyfiles:
        if 'c' in f:
            candidate_goals.append(enc_dec.encode(path_dir+'/'+f, True))

    try:
        os.makedirs(path_output)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    create_problem(init, goal, path_output + '/problem_neg.pddl')
    create_problem_no_negatives(init, goal, path_output + '/problem.pddl')
    if plan:
        print("Planning: ", path_domain, path_dir)
        plan_mp(path_domain, path_output+'/problem.pddl')
        print("Done")
    else:
        print("Planning skiped!")
    save_plan_img(cvt_ttotran_MP(init.tolist(),pddl_actions), path_output + '/plan.png', enc_dec, SIZE_H, SIZE_W)
    export_problem_pgr(init, path_output+ '/')
    transitions = cvt_ttotran_MP(init,pddl_actions)
    traces = cvt_trantotrace(cvt_ttotran_MP(init,pddl_actions),pddl_actions)
    p_traces = percentage_slice(traces, float(obs)/100.0)
    call(['cp', path_domain, path_output+ '/' +'domain.pddl'])
    call(['cp', 'sas_plan', path_output+ '/' +'log.txt'])
    export_trace_obs(p_traces, path_output + '/obs.dat')
    export_hypothesis(transitions, path_output + '/obs2.dat')
    export_hypothesis(candidate_goals, path=path_output + '/' + 'hyps.dat')
    export_hypothesis([goal], path=path_output+ '/' +'real_hyp.dat')
    online_req(traces,candidate_goals, goal)



def online_req(traces, possible_goals, goal):
    import subprocess

    p = subprocess.Popen(
        [
            'java',  
            '-cp',
            ONLINE_REQ_JAR,
            'MyProg'
        ],
        stdout = subprocess.PIPE, 
        stdin = subprocess.PIPE,
    )
    for t in traces:
        #p.stdin.write(str(trace))
        #print(t)
        print("Sending", t)
        #print p.stdout.readline().rstrip()

def parse_obs_data(path):
    data = open(path, 'r')
    obs = []    
    for d in data:
        bit_rep = parse_pddl_state(d)
        obs.append(bit_rep)
    return obs

#converts a pddl state to a bit representation
def parse_pddl_state(pddl, size, remove_not=False):
    output = [0] * size
    if remove_not:
        new_pddl = ""
        split = pddl.split(",")
        for s in split:
            if "not" in s:
                continue
            else new_pddl += str(s)
        pddl = new_pddl
    pddl_split = pddl.replace(" ", "").replace(",","").replace(")","").replace("(","").replace("\n","").replace("[","").replace("]","")
    pddl_split = filter(None ,pddl_split.split('p'))
    for pddl in pddl_split:
        output[int(pddl)] = 1
    return output

if __name__ == '__main__':
    import sys
    if sys.argv[1] == 'domain':
        module_create_domain(*sys.argv[2:])
    elif sys.argv[1] == 'recon':
        set_up_pgr(*sys.argv[2:])
    elif sys.argv[1] == 'online':
        set_up_online_pgr(*sys.argv[2:])       
    #if len(sys.argv) < 3:
     #   sys.exit("{} [networkdir] [problemdir]".format(sys.argv[0]))
    #main(*sys.argv[1:])
    sys.exit()
#set_up_pgr('samples/puzzle_mnist_3_3_36_20000_conv/','mnist01/domain.pddl', 'pb01', 'pb01_out')
