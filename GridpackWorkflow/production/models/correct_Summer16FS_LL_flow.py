import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps

#set dev to False to run the final version of the script (i.e. send the modifications made to MCM)
#while editing keep dev set to True
mcm = McM(dev=False)

#list of requests to extend 
requests_to_modify = list('SUS-RunIISummer16DR80Premix-00' + str(i) for i in range(372,372+1) )

#write the prepids of the new cloned requests to a txt file
f = open('new_requests.txt', 'w')

for request_prepid_to_modify in requests_to_modify:
    
    print( 'Modifying and modifying {0}'.format(request_prepid_to_modify) )

    # Get a request object which we want to clone
    request = mcm.get('requests', request_prepid_to_modify)
    
    if 'LLChipm' not in request['dataset_name']: continue

    request['sequences'][0]['outputCommand'] = "'keep *_genParticlePlusGeant_*_*'" 
    request['sequences'][0]['customise'] = 'SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeProduce,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeKeep'

    request['sequences'][1]['outputCommand'] = "'keep *_genParticlePlusGeant_*_*'" 
    request['sequences'][1]['customise'] = 'SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeProduce,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeKeep'

    #update the cloned request
    update_response = mcm.update('requests', request)
    updated_clone = mcm.get('requests',  request_prepid_to_modify)
    
f.close()
