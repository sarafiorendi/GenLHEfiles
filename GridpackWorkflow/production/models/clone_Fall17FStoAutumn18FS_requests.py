import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps

#set dev to False to run the final version of the script (i.e. send the modifications made to MCM)
#while editing keep dev set to True
mcm = McM(dev=False)

#list of requests to clone 
#requests_to_clone = [ 'SUS-RunIIFall17FSPremix-00120',
#                      'SUS-RunIIFall17FSPremix-00121', 
#                       ] 
requests_to_clone = [ ]
ist0 = list('SUS-RunIIFall17FSPremix-00' + str(i) for i in range(156,160+1))
for req in list0:
    requests_to_clone.append(req)

#write the prepids of the new cloned requests to a txt file
f = open('new_requests.txt', 'w')

# If member_of_campaign is different, it will clone to other campaign
campaign_modifications = {'member_of_campaign': 'RunIIAutumn18FSPremix'}

for request_prepid_to_clone in requests_to_clone:
    
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
