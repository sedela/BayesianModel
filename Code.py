print("Network written to Network.xdsl")
print("Inferences are successfully done")





#Description :This code is written with a python wrapper of a C++ library called " Structural Modeling, Inference and Learning Engine(SMILE) it contains two classes, one for the creation of a Bayesian network that models the causal relationships between metacognitive skills and their influence on the level of self-regulation. The other class is for the modification of the values of each evidence and the  beliefs update (Bayesian inference). It is necessary to import a "pysmile" package from the site https://www.bayesfusion.com/


import pysmile
import pysmile_license

class CreatingBN:


    def __init__(self):
        net = pysmile.Network()
#Defining of nodes

        lof = self.create_cpt_node(net,"Level_of_SelfRegulation", "Level of Self-regulation",["Bad","Intermediate","Good"],200, 40)
        eng = self.create_fcpt_node(net,"Engage_in_Learning_Goals", "Engage in Learning Goals",["NotLearned","InProgress","Learned"],160, 48)
        eval = self.create_cpt_node(net,"MonitorEvaluateProgress", "Evaluate and Monitor the progress",["NotLearned","InProgress","Learned"],110, 140)
        under = self.create_cpt_node(net,"Understand_and_describe_Goals_Plan", "Understand and describe Goals ( Plan )",["NotLearned","InProgress","Learned"],111, 160)
        mang = self.create_cpt_node(net,"Manage_the_obstacles_Challenges", "Manage the obstacles/Challenges",["NotLearned","InProgress","Learned"],98, 170)
        res = self.create_cpt_node(net,"ResourceManagement", "Manage the Resources",["NotLearned","InProgress","Learned"],141, 180)
        htd = self.create_cpt_node(net,"HowToDo", "Execute Tasks (How To Do)",["NotLearned","InProgress","Learned"],181, 98)
        task = self.create_cpt_node(net,"Identify_and_Descibe_tasks", "Identify and Descibe tasks",["NotLearned","InProgress","Learned"],171, 150)
        react = self.create_cpt_node(net,"React_to_different_situations_Adaptability", "React to different situations / Adaptability",["NotLearned","InProgress","Learned"],45, 180)
#Defining of arcs
        net.add_arc(eng, lof)
        net.add_arc(eval, lof)
        net.add_arc(under, eng)
        net.add_arc(eng, task)
        net.add_arc(react, task)
        net.add_arc(task, res)
        net.add_arc(res, htd)
        net.add_arc(htd, mang)
        net.add_arc(mang, eval)


#Defining of Conditional Probability Table (CPT) for each node


        underCPT = [

            0.091856061, # P(under=N)
            0.38162879, # P(under=I)
            0.52651515 # P(under=L)
        ]

        net.set_node_definition(under, underCPT)

        reactCPT = [

            0.1174242424242424, # P(react=N)
            0.4839015151515152, # P(react=I)
            0.3986742424242424 # P(react=L)
        ]

        net.set_node_definition(react, reactCPT)



        evalCPT = [
    #--------State=NotLearned
                0.27693333, # P(eval=N|mang=N)
                0.229771138561716, # P(eval=N|mang=I)
                0.1561223732085839, # P(eval=N|mang=L)
    #--------State=InProgress
                0.4649333333333333, # P(eval=I|mang=N)
                0.5256631236234798, # P(eval=I|mang=I)
                0.6753916982252913, # P(eval=I|mang=L)
    #--------State=Learned
                0.2581333333333333, # P(eval=L|mang=N)
                0.2445657378148041, # P(eval=L|mang=I)
                0.1684859285661246 # P(eval=L|mang=L)
                       ]

        net.set_node_definition(eval, evalCPT)

        engCPT = [
            #--------State=NotLearned
                        0.3482304422842233, # P(eng=N|under=N)
                        0.324035516777932, # P(eng=N|under=I)
                        0.2131292517006803, # P(eng=N|under=L)
            #--------State=InProgress
                        0.3258847788578882, # P(eng=I|under=N)
                        0.4216625906096459, # P(eng=I|under=I)
                        0.4341496598639455, # P(eng=I|under=L)
            #--------State=Learned
                        0.3258847788578882, # P(eng=L|under=N)
                        0.2543018926124221, # P(eng=L|under=I)
                        0.3527210884353741 # P(eng=L|under=L)
                               ]

        net.set_node_definition(eng, engCPT)

        mangCPT = [
            #--------State=NotLearned
                        0.2606293333333333, # P(mang=N|htd=N)
                        0.2230315643426986, # P(mang=N|htd=I)
                        0.2613190058755145, # P(mang=N|htd=L)
            #--------State=InProgress
                        0.3424213333333334, # P(mang=I|htd=N)
                        0.3057578910856746, # P(mang=I|htd=I)
                        0.3693404970622428, # P(mang=I|htd=L)
            #--------State=Learned
                        0.3969493333333333, # P(mang=L|htd=N)
                        0.4712105445716268, # P(mang=L|htd=I)
                        0.3693404970622428 # P(mang=L|htd=L)
                               ]

        net.set_node_definition(mang, mangCPT)

        htdCPT = [
            #--------State=NotLearned
                        0.2606293333333333, # P(htd=N|res=N)
                        0.2230315643426986, # P(htd=N|res=I)
                        0.2613190058755145, # P(htd=N|res=L)
            #--------State=InProgress
                        0.3424213333333334, # P(htd=I|res=N)
                        0.3057578910856746, # P(htd=I|res=I)
                        0.3693404970622428, # P(htd=I|res=L)
            #--------State=Learned
                        0.3969493333333333, # P(htd=L|res=N)
                        0.4712105445716268, # P(htd=L|res=I)
                        0.3693404970622428 # P(htd=L|res=L)
                               ]

        net.set_node_definition(htd, htdCPT)

        taskCPT = [
#--------State=NotLearned
            0.3333333333333333, # P(task=N|eng=N|react=N)
            0.3062973222530009, # P(task=N|eng=N|react=I)
            0.3145333333333334, # P(task=N|eng=N|react=L)

            0.3406584362139918, # P(task=N|eng=I|react=N)
            0.4130527210884354, # P(task=N|eng=I|react=I)
            0.2988014714607808, # P(task=N|eng=I|react=L)

            0.3626337448559671, # P(task=N|eng=L|react=N)
            0.4161735700197238, # P(task=N|eng=L|react=I)
            0.3265743305632502, # P(task=N|eng=L|react=L)
#--------State=InProgress
            0.3333333333333333, # P(task=I|eng=N|react=N)
            0.3468513388734995, # P(task=I|eng=N|react=I)
            0.3145333333333334, # P(task=I|eng=N|react=L)

            0.3406584362139918, # P(task=I|eng=I|react=N)
            0.3333333333333333, # P(task=I|eng=I|react=I)
            0.4196629880147146, # P(task=I|eng=I|react=L)

            0.3186831275720165, # P(task=I|eng=L|react=N)
            0.3274161735700197, # P(task=I|eng=L|react=I)
            0.3468513388734996, # P(task=I|eng=L|react=L)
#--------State=Learned
            0.3333333333333333, # P(task=L|eng=N|react=N)
            0.3468513388734995, # P(task=L|eng=N|react=I)
            0.3709333333333333, # P(task=L|eng=N|react=L)

            0.3186831275720165, # P(task=L|eng=I|react=N)
            0.2536139455782313, # P(task=L|eng=I|react=I)
            0.2815355405245045, # P(task=L|eng=I|react=L)

            0.3186831275720165, # P(task=L|eng=L|react=N)
            0.2564102564102564, # P(task=L|eng=L|react=I)
            0.3265743305632502 # P(task=L|eng=L|react=L)


        ]

        net.set_node_definition(task, taskCPT)

        resCPT = [
#--------State=NotLearned
            0.4023970570784384, # P(res=N|task=N)
            0.4053476607911521, # P(res=N|task=I)
            0.3549490802238055, # P(res=N|task=L)


#--------State=InProgress
            0.3505992642696095, # P(res=I|task=N)
            0.351336915197788, # P(res=I|task=I)
            0.3117175864428612, # P(res=I|task=L)


#--------State=Learned
            0.2470036786519521, # P(res=L|task=N)
            0.2433154240110598, # P(res=L|task=I)
            0.3333333333333334, # P(res=L|task=L)

           ]

        net.set_node_definition(res, resCPT)

        lofCPT = [
#--------State=Bad
            0.1, # P(lof=B|eval=N|eng=N)
            0.3, # P(lof=B|eval=N|eng=I)
            0.0, # P(lof=B|eval=N|eng=L)

            0.1, # P(lof=B|eval=I|eng=N)
            0.1, # P(lof=B|eval=I|eng=I)
            0.1, # P(lof=B|eval=I|eng=L)

            0.1, # P(lof=B|eval=L|eng=N)
            0.1, # P(lof=B|eval=L|eng=I)
            0.1, # P(lof=B|eval=L|eng=L)
#--------State=Intermediate
            0.5, # P(lof=I|eval=N|eng=N)
            0.4, # P(lof=I|eval=N|eng=I)
            0.6, # P(lof=I|eval=N|eng=L)

            0.5, # P(lof=I|eval=I|eng=N)
            0.5, # P(lof=I|eval=I|eng=I)
            0.6, # P(lof=I|eval=I|eng=L)

            0.6, # P(lof=I|eval=L|eng=N)
            0.6, # P(lof=I|eval=L|eng=I)
            0.6, # P(lof=I|eval=L|eng=L)
#--------State=Good
            0.4, # P(lof=G|eval=N|eng=N)
            0.3, # P(lof=G|eval=N|eng=I)
            0.4, # P(lof=G|eval=N|eng=L)

            0.4, # P(lof=G|eval=I|eng=N)
            0.4, # P(lof=G|eval=I|eng=I)
            0.3, # P(lof=G|eval=I|eng=L)

            0.3, # P(lof=G|eval=L|eng=N)
            0.3, # P(lof=G|eval=L|eng=I)
            0.3 # P(lof=G|eval=L|eng=L)


        ]

        net.set_node_definition(lof, lofCPT)



#save the file "Network.xdsl" in the current directory
        net.write_file("Network.xdsl")
        print("Network written to Network.xdsl")



def create_cpt_node(self, net, id, name, outcomes, x_pos, y_pos):

    handle = net.add_node(pysmile.NodeType.CPT, id)



    net.set_node_name(handle, name)

    net.set_node_position(handle, x_pos, y_pos, 85, 55)



    initial_outcome_count = net.get_outcome_count(handle)



    for i in range(0, initial_outcome_count):

        net.set_outcome_id(handle, i, outcomes[i])



    for i in range(initial_outcome_count, len(outcomes)):

        net.add_outcome(handle, outcomes[i])



    return handle
#---------------------------------------------------------------------

    #performs the series of inference calls

class InferenceCalls:

    def __init__(self):

        net = pysmile.Network()

    # load the network created in the class CreatingBN

        net.read_file("Network.xdsl")


#Update the probabilities and  display them using the method print_all_posteriors() defined below
        print("Posteriors with no evidence set:")

        net.update_beliefs()

        self.print_all_posteriors(net)


#Fix the state of each node using its id
        print("Setting  Engage_in_Learning_Goals =Learned.")

        self.change_evidence_and_update(net, "Engage_in_Learning_Goals", "Learned")

        print("MonitorEvaluateProgress=InProgress.")

        self.change_evidence_and_update(net, "MonitorEvaluateProgress", "InProgress")



        print("Changing MonitorEvaluateProgress to NotLearned, Keeping  Engage_in_Learning_Goals=Learned.")

        self.change_evidence_and_update(net, "MonitorEvaluateProgress", "NotLearned")



        print("Removing evidence from  Engage_in_Learning_Goals , keeping MonitorEvaluateProgress=NotLearned.")

        self.change_evidence_and_update(net, "Engage_in_Learning_Goals", None)

        print("Inferences are successfully done")

#Definig the used methods

    def print_posteriors(self, net, node_handle):

        node_id = net.get_node_id(node_handle)

        if net.is_evidence(node_handle):

            #print(node_id + " has evidence set (" +net.get_outcome_id(node_handle, net.get_evidence(node_handle)) + ")")

            ListOfEvidencesStates = Liste (net.get_outcome_id(node_handle, net.get_evidence(node_handle)))
            posteriors1 = net.get_node_value(node_handle)
            for i in range(0, len(posteriors1)):

                print("P(" + node_id + "|" + ListOfEvidencesStates +")=" + str(posteriors1[i]))
        else:

            posteriors2 = net.get_node_value(node_handle)

            for i in range(0, len(posteriors2)):

                print("P(" + node_id + "=" + net.get_outcome_id(node_handle, i) +")=" + str(posteriors2[i]))



    def print_all_posteriors(self, net):

        handle = net.get_first_node()

        while (handle >= 0):

            self.print_posteriors(net, handle)

            handle = net.get_next_node(handle)





    def change_evidence_and_update(self, net, node_id, outcome_id):

        if outcome_id is not None:

            net.set_evidence(node_id, outcome_id)

        else:

            net.clear_evidence(node_id)



        net.update_beliefs()

        self.print_all_posteriors(net)
