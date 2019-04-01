import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps

#set dev to False to run the final version of the script (i.e. send the modifications made to MCM). While editing keep dev set to True
mcm = McM(dev=True)

# ctau values
ctau_values = [ 'ctau-10', 'ctau-50', 'ctau-200' ]

# List of models, with their mother request and LSP mass points
models = { 'T1qqqq-LLChipm'   : { 'mother_request' : 'SUS-RunIISummer15GS-00229',
                                  'massLSP' : { '1' : { 'nev' : '539000', 'meff' : '0.279'},
                                                '200' : { 'nev' : '539000', 'meff' : '0.279'},
                                                '400' : { 'nev' : '539000', 'meff' : '0.279'},
                                                '600' : { 'nev' : '539000', 'meff' : '0.279'},
                                                '800' : { 'nev' : '791000', 'meff' : '0.269'},
                                                '900' : { 'nev' : '631000', 'meff' : '0.251'},
                                                '975' : { 'nev' : '150000', 'meff' : '0.235'},
                                                '1000' : { 'nev' : '681000', 'meff' : '0.278'},
                                                '1075' : { 'nev' : '132000', 'meff' : '0.235'},
                                                '1100' : { 'nev' : '429000', 'meff' : '0.271'},
                                                '1175' : { 'nev' : '69000', 'meff' : '0.245'},
                                                '1200' : { 'nev' : '520000', 'meff' : '0.296'},
                                                '1275' : { 'nev' : '40000', 'meff' : '0.245'},
                                                '1300' : { 'nev' : '400000', 'meff' : '0.287'},
                                                '1375' : { 'nev' : '40000', 'meff' : '0.255'},
                                                '1400' : { 'nev' : '480000', 'meff' : '0.305'},
                                                '1475' : { 'nev' : '40000', 'meff' : '0.267'},
                                                '25' : { 'nev' : '520000', 'meff' : '0.315'},
                                                '50' : { 'nev' : '520000', 'meff' : '0.315'},
                                                '75' : { 'nev' : '520000', 'meff' : '0.315'},
                                                '150' : { 'nev' : '520000', 'meff' : '0.315'},
                                                '1500' : { 'nev' : '400000', 'meff' : '0.303'},
                                                '1575' : { 'nev' : '40000', 'meff' : '0.267'},
                                                '1600' : { 'nev' : '440000', 'meff' : '0.315'},
                                                '1675' : { 'nev' : '40000', 'meff' : '0.267'},
                                                '1700' : { 'nev' : '400000', 'meff' : '0.320'},
                                                '1775' : { 'nev' : '40000', 'meff' : '0.290'},
                                                '1800' : { 'nev' : '400000', 'meff' : '0.327'},
                                                '1875' : { 'nev' : '40000', 'meff' : '0.290'},
                                                '1900' : { 'nev' : '360000', 'meff' : '0.331'},
                                                '1975' : { 'nev' : '40000', 'meff' : '0.290'},
                                                '2000' : { 'nev' : '320000', 'meff' : '0.337'},
                                                '2075' : { 'nev' : '40000', 'meff' : '0.315'},
                                                '2100' : { 'nev' : '280000', 'meff' : '0.340'},
                                                '2175' : { 'nev' : '40000', 'meff' : '0.315'},
                                                '2200' : { 'nev' : '240000', 'meff' : '0.344'},
                                                '2275' : { 'nev' : '40000', 'meff' : '0.315'},
                                                '2300' : { 'nev' : '200000', 'meff' : '0.350'},
                                                '2375' : { 'nev' : '40000', 'meff' : '0.340'},
                                                '2400' : { 'nev' : '160000', 'meff' : '0.352'},
                                                '2475' : { 'nev' : '40000', 'meff' : '0.340'},
                                                '2500' : { 'nev' : '120000', 'meff' : '0.356'},
                                                '2575' : { 'nev' : '40000', 'meff' : '0.340'},
                                                '2600' : { 'nev' : '80000', 'meff' : '0.364'},
                                                '2675' : { 'nev' : '40000', 'meff' : '0.364'},
                                                '2700' : { 'nev' : '40000', 'meff' : '0.364'},
                                                '2775' : { 'nev' : '40000', 'meff' : '0.364'},
                                                },
                                  }, 
           'T2qq-LLChipm'     : { 'mother_request' : '',
                                  'massLSP' : { '1' : { 'nev' : '1831000', 'meff' : '0.264'},
                                                '100' : { 'nev' : '1831000', 'meff' : '0.264'},
                                                '200' : { 'nev' : '2581000', 'meff' : '0.268'},
                                                '250' : { 'nev' : '1891000', 'meff' : '0.274'},
                                                '275' : { 'nev' : '857000', 'meff' : '0.267'},
                                                '300' : { 'nev' : '1974000', 'meff' : '0.265'},
                                                '325' : { 'nev' : '855000', 'meff' : '0.256'},
                                                '350' : { 'nev' : '1250000', 'meff' : '0.259'},
                                                '375' : { 'nev' : '947000', 'meff' : '0.247'},
                                                '400' : { 'nev' : '1382000', 'meff' : '0.258'},
                                                '425' : { 'nev' : '1008000', 'meff' : '0.246'},
                                                '450' : { 'nev' : '750000', 'meff' : '0.248'},
                                                '475' : { 'nev' : '1050000', 'meff' : '0.241'},
                                                '500' : { 'nev' : '840000', 'meff' : '0.255'},
                                                '525' : { 'nev' : '1079000', 'meff' : '0.241'},
                                                '550' : { 'nev' : '250000', 'meff' : '0.237'},
                                                '575' : { 'nev' : '1099000', 'meff' : '0.237'},
                                                '225' : { 'nev' : '250000', 'meff' : '0.237'},
                                                '625' : { 'nev' : '869000', 'meff' : '0.237'},
                                                '675' : { 'nev' : '639000', 'meff' : '0.237'},
                                                '725' : { 'nev' : '443000', 'meff' : '0.237'},
                                                '775' : { 'nev' : '324000', 'meff' : '0.237'},
                                                '825' : { 'nev' : '252000', 'meff' : '0.237'},
                                                '875' : { 'nev' : '211000', 'meff' : '0.238'},
                                                '925' : { 'nev' : '189000', 'meff' : '0.238'},
                                                '975' : { 'nev' : '180000', 'meff' : '0.239'},
                                                '1025' : { 'nev' : '180000', 'meff' : '0.240'},
                                                '600' : { 'nev' : '320000', 'meff' : '0.271'},
                                                '1075' : { 'nev' : '180000', 'meff' : '0.241'},
                                                '1125' : { 'nev' : '180000', 'meff' : '0.242'},
                                                '700' : { 'nev' : '300000', 'meff' : '0.273'},
                                                '1175' : { 'nev' : '180000', 'meff' : '0.243'},
                                                '1225' : { 'nev' : '180000', 'meff' : '0.244'},
                                                '800' : { 'nev' : '280000', 'meff' : '0.276'},
                                                '1275' : { 'nev' : '180000', 'meff' : '0.245'},
                                                '1325' : { 'nev' : '180000', 'meff' : '0.245'},
                                                '900' : { 'nev' : '260000', 'meff' : '0.278'},
                                                '1375' : { 'nev' : '180000', 'meff' : '0.245'},
                                                '1425' : { 'nev' : '180000', 'meff' : '0.248'},
                                                '1000' : { 'nev' : '240000', 'meff' : '0.281'},
                                                '1475' : { 'nev' : '180000', 'meff' : '0.251'},
                                                '1525' : { 'nev' : '180000', 'meff' : '0.253'},
                                                '1100' : { 'nev' : '220000', 'meff' : '0.284'},
                                                '1575' : { 'nev' : '180000', 'meff' : '0.255'},
                                                '1625' : { 'nev' : '180000', 'meff' : '0.260'},
                                                '1200' : { 'nev' : '200000', 'meff' : '0.288'},
                                                '1675' : { 'nev' : '180000', 'meff' : '0.264'},
                                                '1725' : { 'nev' : '180000', 'meff' : '0.269'},
                                                '1300' : { 'nev' : '180000', 'meff' : '0.293'},
                                                '1775' : { 'nev' : '180000', 'meff' : '0.274'},
                                                '1825' : { 'nev' : '180000', 'meff' : '0.282'},
                                                '1400' : { 'nev' : '160000', 'meff' : '0.298'},
                                                '1875' : { 'nev' : '180000', 'meff' : '0.288'},
                                                '1925' : { 'nev' : '180000', 'meff' : '0.294'},
                                                '1500' : { 'nev' : '140000', 'meff' : '0.303'},
                                                '1975' : { 'nev' : '180000', 'meff' : '0.299'},
                                                '2025' : { 'nev' : '180000', 'meff' : '0.305'},
                                                '1600' : { 'nev' : '120000', 'meff' : '0.309'},
                                                '2075' : { 'nev' : '180000', 'meff' : '0.309'},
                                                '2125' : { 'nev' : '180000', 'meff' : '0.313'},
                                                '1700' : { 'nev' : '100000', 'meff' : '0.313'},
                                                '2175' : { 'nev' : '180000', 'meff' : '0.316'},
                                                '1800' : { 'nev' : '80000', 'meff' : '0.320'},
                                                '1900' : { 'nev' : '60000', 'meff' : '0.320'},
                                                '2000' : { 'nev' : '40000', 'meff' : '0.320'},
                                                '2100' : { 'nev' : '20000', 'meff' : '0.320'},
                                                }
                                  },  
           'T2bt-LLChipm'     : { 'mother_request' : '',
                                  'massLSP' : { '1' : { 'nev' : '2291000', 'meff' : '0.266'},
                                                '50' : { 'nev' : '2291000', 'meff' : '0.266'},
                                                '100' : { 'nev' : '2291000', 'meff' : '0.266'},
                                                '150' : { 'nev' : '2291000', 'meff' : '0.266'},
                                                '200' : { 'nev' : '4219000', 'meff' : '0.282'},
                                                '250' : { 'nev' : '3339000', 'meff' : '0.269'},
                                                '300' : { 'nev' : '2848000', 'meff' : '0.267'},
                                                '315' : { 'nev' : '730000', 'meff' : '0.275'},
                                                '350' : { 'nev' : '1873000', 'meff' : '0.260'},
                                                '365' : { 'nev' : '377000', 'meff' : '0.275'},
                                                '400' : { 'nev' : '1367000', 'meff' : '0.257'},
                                                '415' : { 'nev' : '206000', 'meff' : '0.254'},
                                                '450' : { 'nev' : '1089000', 'meff' : '0.255'},
                                                '465' : { 'nev' : '118000', 'meff' : '0.254'},
                                                '500' : { 'nev' : '929000', 'meff' : '0.256'},
                                                '515' : { 'nev' : '70000', 'meff' : '0.237'},
                                                '550' : { 'nev' : '835000', 'meff' : '0.259'},
                                                '565' : { 'nev' : '43000', 'meff' : '0.237'},
                                                '600' : { 'nev' : '787000', 'meff' : '0.260'},
                                                '615' : { 'nev' : '27000', 'meff' : '0.237'},
                                                '650' : { 'nev' : '760000', 'meff' : '0.261'},
                                                '665' : { 'nev' : '20000', 'meff' : '0.237'},
                                                '700' : { 'nev' : '740000', 'meff' : '0.261'},
                                                '715' : { 'nev' : '20000', 'meff' : '0.237'},
                                                '750' : { 'nev' : '720000', 'meff' : '0.262'},
                                                '765' : { 'nev' : '20000', 'meff' : '0.237'},
                                                '800' : { 'nev' : '700000', 'meff' : '0.263'},
                                                '815' : { 'nev' : '20000', 'meff' : '0.237'},
                                                '850' : { 'nev' : '680000', 'meff' : '0.264'},
                                                '865' : { 'nev' : '20000', 'meff' : '0.237'},
                                                '900' : { 'nev' : '660000', 'meff' : '0.264'},
                                                '915' : { 'nev' : '20000', 'meff' : '0.237'},
                                                '950' : { 'nev' : '640000', 'meff' : '0.265'},
                                                '965' : { 'nev' : '20000', 'meff' : '0.237'},
                                                '1000' : { 'nev' : '620000', 'meff' : '0.266'},
                                                '1015' : { 'nev' : '20000', 'meff' : '0.237'},
                                                '1050' : { 'nev' : '600000', 'meff' : '0.267'},
                                                '1065' : { 'nev' : '20000', 'meff' : '0.237'},
                                                '1100' : { 'nev' : '580000', 'meff' : '0.268'},
                                                '1115' : { 'nev' : '20000', 'meff' : '0.237'},
                                                '1150' : { 'nev' : '560000', 'meff' : '0.270'},
                                                '1165' : { 'nev' : '20000', 'meff' : '0.237'},
                                                '1200' : { 'nev' : '540000', 'meff' : '0.271'},
                                                '1215' : { 'nev' : '20000', 'meff' : '0.243'},
                                                '1250' : { 'nev' : '520000', 'meff' : '0.272'},
                                                '1265' : { 'nev' : '20000', 'meff' : '0.243'},
                                                '1300' : { 'nev' : '500000', 'meff' : '0.273'},
                                                '1315' : { 'nev' : '20000', 'meff' : '0.243'},
                                                '1350' : { 'nev' : '480000', 'meff' : '0.275'},
                                                '1365' : { 'nev' : '20000', 'meff' : '0.243'},
                                                '1400' : { 'nev' : '460000', 'meff' : '0.276'},
                                                '1415' : { 'nev' : '20000', 'meff' : '0.246'},
                                                '1450' : { 'nev' : '440000', 'meff' : '0.277'},
                                                '1465' : { 'nev' : '20000', 'meff' : '0.246'},
                                                '1500' : { 'nev' : '420000', 'meff' : '0.279'},
                                                '1515' : { 'nev' : '20000', 'meff' : '0.246'},
                                                '1550' : { 'nev' : '400000', 'meff' : '0.281'},
                                                '1565' : { 'nev' : '20000', 'meff' : '0.246'},
                                                '1600' : { 'nev' : '380000', 'meff' : '0.282'},
                                                '1615' : { 'nev' : '20000', 'meff' : '0.246'},
                                                '1650' : { 'nev' : '360000', 'meff' : '0.287'},
                                                '1665' : { 'nev' : '20000', 'meff' : '0.246'},
                                                '1700' : { 'nev' : '340000', 'meff' : '0.289'},
                                                '1715' : { 'nev' : '20000', 'meff' : '0.246'},
                                                '1750' : { 'nev' : '320000', 'meff' : '0.292'},
                                                '1765' : { 'nev' : '20000', 'meff' : '0.267'},
                                                '1800' : { 'nev' : '300000', 'meff' : '0.294'},
                                                '1815' : { 'nev' : '20000', 'meff' : '0.267'},
                                                '1850' : { 'nev' : '280000', 'meff' : '0.298'},
                                                '1865' : { 'nev' : '20000', 'meff' : '0.267'},
                                                '1900' : { 'nev' : '260000', 'meff' : '0.301'},
                                                '1915' : { 'nev' : '20000', 'meff' : '0.267'},
                                                '1950' : { 'nev' : '240000', 'meff' : '0.303'},
                                                '1965' : { 'nev' : '20000', 'meff' : '0.287'},
                                                '2000' : { 'nev' : '220000', 'meff' : '0.305'},
                                                }
                                  },  
           }

#write the prepids of the new cloned requests to a txt file
f = open('new_requests.txt', 'w')

for model in models:

    if  'mother_request' in models[model].keys() :
        if models[model]['mother_request']!='' :
            
            print( 'Cloning and modifying {0}'.format(models[model]['mother_request']) )

            # Get a request object which we want to clone
            request = mcm.get('requests', models[model]['mother_request'])

            #if not request.get('results') :
            #    print '   Request', models[model]['mother_request'], 'not found'
            #    continue

            #print request['generator_parameters'][0]['match_efficiency']

            model_mother = ctau_mother = mLSP_mother = massLSP_mother = ''
            datasetname = request['dataset_name'].split('_')
            for datastring in datasetname :
                if 'SMS-T' in datastring :
                    model_mother = datastring.replace('SMS-', '')
                elif 'ctau' in datastring :
                    ctau_mother = datastring
                elif 'mLSP' in datastring :
                    mLSP_mother = datastring
                    massLSP_mother = datastring.replace('mLSP-', '')

            if ctau_mother=='' or mLSP_mother=='' :
                continue

            for ctau_value in ctau_values :

                update_dataset_name = request['dataset_name'].replace(ctau_mother,ctau_value)

                update_fragment = request['fragment'].replace('model = "'+model_mother+'_'+ctau_mother+'"', 'model = "'+model_mother+'_'+ctau_value+'"')
                if ctau_value!=ctau_mother :
                    update_fragment = update_fragment.replace('ctau = ',     '#ctau = ') 
                    update_fragment = update_fragment.replace('DeltaM = ',   '#DeltaM = ') 
                    update_fragment = update_fragment.replace('ChiWidth = ', '#ChiWidth = ') 
                    if ctau_value=='ctau-10' :                                
                        update_fragment = update_fragment.replace('##ctau =  "10cm"',                     'ctau =  "10cm"')
                        update_fragment = update_fragment.replace('##DeltaM = 0.32485759',                'DeltaM = 0.32485759')
                        update_fragment = update_fragment.replace('##ChiWidth = 1.97327052176253113e-15', 'ChiWidth = 1.97327052176253113e-15')
                    elif ctau_value=='ctau-50' : 
                        update_fragment = update_fragment.replace('##ctau =  "50cm"',                     'ctau =  "50cm"')
                        update_fragment = update_fragment.replace('##DeltaM = 0.23638902',                'DeltaM = 0.23638902')
                        update_fragment = update_fragment.replace('##ChiWidth = 0.39466403282527335e-15', 'ChiWidth = 0.39466403282527335e-15')
                    elif ctau_value=='ctau-200' : 
                        update_fragment = update_fragment.replace('##ctau = "200cm"',                     'ctau = "200cm"')
                        update_fragment = update_fragment.replace('##DeltaM = 0.18288376',                'DeltaM = 0.18288376') 
                        update_fragment = update_fragment.replace('##ChiWidth = 0.9866600820631833e-16',  'ChiWidth = 0.9866600820631833e-16')
                    else: 
                        print '   Wrong ctau value:', ctau_value
                        continue

                if 'massLSP' in models[model].keys() :
                    for mLSP in models[model]['massLSP'] :

                        if ctau_value==ctau_mother and 'mLSP-'+mLSP==mLSP_mother :
                            continue # do not duplicate the mother
                        
                        if mLSP!='400' and mLSP!='1000' :
                            continue

                        #clone request and print error if it fails 
                        clone_answer = mcm.clone_request(request)
                        if not clone_answer.get('results'): 
                            print('Something went wrong while cloning a request. %s' % (dumps(clone_answer)))
                            continue

                        #write new prepid to file 
                        f.write( clone_answer['prepid'] + '\n')
                        
                        #modify and update cloned request
                        #note that these modifications must be done after cloning since they might otherwise be reset
                        cloned_request = mcm.get('requests', clone_answer['prepid'] )

                        mass_dataset_name = update_dataset_name.replace(mLSP_mother, 'mLSP-'+mLSP)

                        mass_fragment = update_fragment.replace('mLSP = '+massLSP_mother, 'mLSP = '+mLSP)
                        mass_fragment = mass_fragment.replace('mcm_eff = ', 'mcm_eff = '+models[model]['massLSP'][mLSP]['meff']+' #')

                        modifications = {'dataset_name' : mass_dataset_name,
                                         'fragment' : mass_fragment,
                                         'extension': 0,
                                         'total_events': int(models[model]['massLSP'][mLSP]['nev']),
                                         'process_string' : '',
                                         'keep_output' : [False], # It is GS, for Falso also for long lived
                                         } 

                        # Make predefined modifications
                        for key in modifications:
                            cloned_request[key] = modifications[key]
   
                        matcheff = float(int(1000*float(models[model]['massLSP'][mLSP]['meff'])*1.072))/1000 
                        cloned_request['generator_parameters'][0]['match_efficiency'] = matcheff

                        print mass_dataset_name
                        print cloned_request['generator_parameters'][0]['match_efficiency'], cloned_request['total_events']
                        #print cloned_request['fragment']

                        #update the cloned request
                        update_response = mcm.update('requests', cloned_request)
                        updated_clone = mcm.get('requests',  clone_answer['prepid'])
 
f.close()
