import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps

#set dev to False to run the final version of the script (i.e. send the modifications made to MCM)
#while editing keep dev set to True
mcm = McM(dev=True)

#list of requests to extend 
requests_to_extend = [ 'SUS-RunIIFall17FSPremix-00065', 'SUS-RunIIFall17FSPremix-00073', 'SUS-RunIIFall17FSPremix-00074',  
                       'SUS-RunIIFall17FSPremix-00064', 'SUS-RunIIFall17FSPremix-00075', 'SUS-RunIIFall17FSPremix-00076',  
                       'SUS-RunIIFall17FSPremix-00068', 'SUS-RunIIFall17FSPremix-00077', 'SUS-RunIIFall17FSPremix-00078',  
                       ]

#write the prepids of the new cloned requests to a txt file
f = open('new_requests.txt', 'w')

for request_prepid_to_clone in requests_to_extend:
    
    print( 'Cloning and modifying {0}'.format(request_prepid_to_clone) )

    # Get a request object which we want to clone
    request = mcm.get('requests', request_prepid_to_clone)
   
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
                     #'total_events': int(total_events),
                     'process_string' : '',
                     'memory' : 4000,
                     'keep_output' : [True], # Special for long-lived models
                     'pileup_dataset_name' : '/Neutrino_E-10_gun/RunIISummer16FSPremix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v4-v1/GEN-SIM-DIGI-RAW',
                     'process_string' : '2016Geometry'
                     'sequences' : {'conditions'   : '80X_mcRun2_asymptotic_2016_TrancheIV_v6',
                                    'beamspot'     : 'Realistic50ns13TeVCollision',
                                    'era'          : 'Run2_2016', # --> is it enough to get the geometry?
                                    'pileup_input' : 'dbs:/Neutrino_E-10_gun/RunIISummer16FSPremix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v4-v1/GEN-SIM-DIGI-RAW',
                                    'geometry'     : '', # --> anything special?
                                    ''             : '', # --> AOB
                                    },
                     }
    
    # Make predefined modifications
    for key in modifications:
        cloned_request[key] = modifications[key]
   
    #update the cloned request
    update_response = mcm.update('requests', cloned_request)
    updated_clone = mcm.get('requests',  clone_answer['prepid'])
    
f.close()
