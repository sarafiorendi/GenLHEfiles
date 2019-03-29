import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps

#set dev to False to run the final version of the script (i.e. send the modifications made to MCM)
#while editing keep dev set to True
mcm = McM(dev=True)

#list of requests to extend 
requests_to_extend = [ 'SUS-RunIIFall17FSPremix-00006', # T1tttt
                       'SUS-RunIIFall17FSPremix-00062', # T1qqqqL
                       'SUS-RunIIFall17FSPremix-00066', 'SUS-RunIIFall17FSPremix-00063', # T1ttbb (+ dM)
                       'SUS-RunIIFall17FSPremix-00032', 'SUS-RunIIFall17FSPremix-00036', # T5qqqqVV (+dM)
                       'SUS-RunIIFall17FSPremix-00112', 'SUS-RunIIFall17FSPremix-00113', # T5ttcc
                       'SUS-RunIIFall17FSPremix-00034', # T5tttt dM
                       'SUS-RunIIFall17FSPremix-00015', 'SUS-RunIIFall17FSPremix-00016', 'SUS-RunIIFall17FSPremix-00017', # T6ttHZ/T6ttWW
                       ] # Block 1
"""
requests_to_extend = [ 'SUS-RunIIFall17FSPremix-00064', 'SUS-RunIIFall17FSPremix-00065', 'SUS-RunIIFall17FSPremix-00068', #  10 cm
                       'SUS-RunIIFall17FSPremix-00073', 'SUS-RunIIFall17FSPremix-00074', 'SUS-RunIIFall17FSPremix-00075', #  50 cm
                       'SUS-RunIIFall17FSPremix-00076', 'SUS-RunIIFall17FSPremix-00077', 'SUS-RunIIFall17FSPremix-00078', # 200 cm
                       'SUS-RunIIFall17FSPremix-00103', 'SUS-RunIIFall17FSPremix-00104', 'SUS-RunIIFall17FSPremix-00105', # T2tb mass ext.
                       'SUS-RunIIFall17FSPremix-00111', # mono-Phi
                       ] # Block 1 LL -> keep output = True !!!
"""
"""
requests_to_extend = [ 'SUS-RunIIFall17FSPremix-00024', # T1bbbb
                       'SUS-RunIIFall17FSPremix-00023', # T1qqqq
                       'SUS-RunIIFall17FSPremix-00021', 'SUS-RunIIFall17FSPremix-00026', # T2qq
                       'SUS-RunIIFall17FSPremix-00019', 'SUS-RunIIFall17FSPremix-00020', # T2bb
                       'SUS-RunIIFall17FSPremix-00013', 'SUS-RunIIFall17FSPremix-00025',  'SUS-RunIIFall17FSPremix-00014', # T2tt
                       'SUS-RunIIFall17FSPremix-00018', 'SUS-RunIIFall17FSPremix-00027', # T2tt cont.
                       'SUS-RunIIFall17FSPremix-00060', 'SUS-RunIIFall17FSPremix-00061', # T2bW/T2tb

                       ] # Block 2
"""

#write the prepids of the new cloned requests to a txt file
f = open('new_requests.txt', 'w')

# If member_of_campaign is different, it will clone to other campaign
campaign_modifications = {'member_of_campaign': 'RunIIAutumn18FSPremix'}

for request_prepid_to_clone in requests_to_extend:
    
    print( 'Cloning and modifying {0}'.format(request_prepid_to_clone) )

    # Get a request object which we want to clone
    request = mcm.get('requests', request_prepid_to_clone)

    # Make predefined modifications
    for key in campaign_modifications:
        request[key] = campaign_modifications[key]

    #clone request and print error if it fails 
    clone_answer = mcm.clone_request(request)
    if clone_answer.get('results'):
        pass
    else:
        print('Something went wrong while cloning a request. %s' % (dumps(clone_answer)))

    #write new prepid to file 
    f.write( clone_answer['prepid'] + '\n')
    
    #modify and update cloned request
    #note that these modifications must be done after cloning since they might otherwise be reset
    cloned_request = mcm.get('requests', clone_answer['prepid'] )

    total_events = request['total_events']
    modifications = {'extension': 0,
                     'total_events': int(total_events*1.5),
                     'process_string' : '',
                     #'memory' : 4000,
                     'keep_output' : [False] 
                     #'keep_output' : [True] # Special for long-lived models
                     }

    # Make predefined modifications
    for key in modifications:
        cloned_request[key] = modifications[key]
   
    #update the cloned request
    update_response = mcm.update('requests', cloned_request)
    updated_clone = mcm.get('requests',  clone_answer['prepid'])
    
f.close()
