import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps

#set dev to False to run the final version of the script (i.e. send the modifications made to MCM)
#while editing keep dev set to True
mcm = McM(dev=False)

#list of requests to clone 
requests_to_clone = [ ]
list0 = list('SUS-RunIISummer15GS-00' + str(i) for i in range(xxx,yyy+1))
for req in list0:
    requests_to_clone.append(req)

#write the prepids of the new cloned requests to a txt file
f = open('new_requests.txt', 'w')

# If member_of_campaign is different, it will clone to other campaign
campaign_modifications = {'member_of_campaign': 'RunIIFall17GS'}

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
    datasetname  = request['dataset_name'].replace('TuneCUETP8M1', 'TuneCP2')
    fragment     = request['fragment']
    fragment     = fragment.replace('from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *', 
                                    'from Configuration.Generator.MCTunes2017.PythiaCP2Settings_cfi import *')
    fragment     = fragment.replace('pythia8CUEP8M1SettingsBlock', 'pythia8CP2SettingsBlock')
    fragment     = fragment.replace('pythia8CUEP8M1Settings',      'pythia8CP2Settings')
    fragment     = fragment.replace('slc6_amd64_gcc481/13TeV/madgraph/V5_2.4.2/sus_sms/', 
                                    '2017/13TeV/madgraph/V5_2.4.2/sus_sms/LO_PDF/')

    modifications = {'dataset_name'   : datasetname,
                     'fragment'       : fragment,
                     #'extension'      : 0,
                     #'total_events'   : int(total_events),
                     #'process_string' : '',
                     #'memory'         : 4000,
                     'keep_output'    : [False] 
                     #'keep_output'    : [True] # Special for long-lived models
                     }

    # Make predefined modifications
    for key in modifications:
        cloned_request[key] = modifications[key]
   
    cloned_request['sequences'][0]['customise_commands'] = '"process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)"'

    #update the cloned request
    update_response = mcm.update('requests', cloned_request)
    updated_clone = mcm.get('requests',  clone_answer['prepid'])
    
f.close()
