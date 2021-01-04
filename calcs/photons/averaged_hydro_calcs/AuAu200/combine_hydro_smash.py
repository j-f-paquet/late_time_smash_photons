import numpy as np
import os
import os.path
import re
import scipy.interpolate

# Format of photon results
#pt	yield	yield*vn_cos[1]	 yield*vn_sin[1]	yield*vn_cos[2]	 yield*vn_sin[2]	yield*vn_cos[3]	 yield*vn_sin[3]	yield*vn_cos[4]	 yield*vn_sin[4]	yield*vn_cos[5]	 yield*vn_sin[5]	yield*vn_cos[6]	 yield*vn_sin[6]

base_directory=os.path.dirname(os.path.realpath(__file__))

###############################################
############## Load calculations ##############
###############################################

result_dict={}
result_dict['smash']={
#'brem':{
#    filename:"../../photon_calcs/smash_calcs/rhic/SP_v2_photons_Brems.txt",
#},
#'22':{
#    filename:"../../photon_calcs/smash_calcs/rhic/SP_v2_photons_2to2.txt",
#},
'tot':{
    'filename_v2':"../../smash_calcs/rhic/SP_v2_photons_total.txt",
    'filename_spectra':"../../smash_calcs/rhic/pT_photons_midy.txt",
},
}
result_dict['hydro']={
'above':{
    'filename':"results/photons_above_Tfr_nx200/AuAu200/C10-20/average_sp.dat",
},
'tot_T140-150':{
    'filename':"results/tot_photons_T140-150_nx200/AuAu200/C10-20/average_sp.dat"
},
'tot_T120-150':{
    'filename':"results/tot_photons_T120-150_nx200/AuAu200/C10-20/average_sp.dat"
},
'tot_T100-150':{
    'filename':"results/tot_photons_T100-150_nx200/AuAu200/C10-20/average_sp.dat"
},
}

# Load everything
for source, source_dict in result_dict.items():

    for channel, channel_dict in source_dict.items():

        if ('smash' == source):
            # Load the v2
            raw=np.loadtxt(channel_dict['filename_v2'])
            pT, v2, v2_err = raw.T

            # Load dN/dpT
            raw=np.loadtxt(channel_dict['filename_spectra'])
            pre_pT, pre_dN_22, pre_dN_22_err, pre_dN_brem, pre_dN_brem_err = raw.T
            dN_22=pre_dN_22/(2*np.pi*pre_pT)
            dN_22_err=pre_dN_22_err/(2*np.pi*pre_pT)
            dN_brem=pre_dN_brem/(2*np.pi*pre_pT)
            dN_brem_err=pre_dN_brem_err/(2*np.pi*pre_pT)
            # Sum channels 
            pre_dN=dN_22+dN_brem
            pre_dN_err=dN_22_err+dN_brem_err
            # Rebin the same way as the v2
            tmp_interp = scipy.interpolate.interp1d(pre_pT, np.log(pre_dN), kind='linear')
            dN=np.exp(tmp_interp(pT))
            tmp_interp = scipy.interpolate.interp1d(pre_pT, np.log(pre_dN_err), kind='linear')
            dN_err=np.exp(tmp_interp(pT))
        else:
            raw=np.loadtxt(channel_dict['filename'])
            pT, dN, v1, v2, *rest = raw.T
            dN_err=np.zeros_like(dN)

        result_dict[source][channel]={
            'pT':pT,
            'dN':dN,
            'dN_err':dN_err,
            'v2':v2
        }
        
#
pT_above=result_dict['hydro']['above']['pT']
dN_above=result_dict['hydro']['above']['dN']
dN_above_err=result_dict['hydro']['above']['dN_err']
v2_above=result_dict['hydro']['above']['v2']

# Make interpolation functions
log_dN_above_interp = scipy.interpolate.interp1d(pT_above, np.log(dN_above), kind='linear', fill_value=np.NaN, bounds_error=False)
log_dN_above_err_interp = scipy.interpolate.interp1d(pT_above, np.log(dN_above_err), kind='linear', fill_value=np.NaN, bounds_error=False)
v2_above_interp = scipy.interpolate.interp1d(pT_above, v2_above, kind='linear', fill_value=np.NaN, bounds_error=False)


def make_destination_dir(tmp_dir):

    if (os.path.isdir(tmp_dir)):
        print("Destination directory ",tmp_dir, " already exists... Aborting.")
        #exit(1)
    else:
        os.makedirs(tmp_dir)

destination_dir=os.path.join(".","combined")
make_destination_dir(destination_dir)

# Combine the results
for source, source_dict in result_dict.items():

    for channel, channel_dict in source_dict.items():

        if ('hydro' == source)and('above' == channel):
            continue
       
        pT_tmp=result_dict[source][channel]['pT']
        dN_tmp=result_dict[source][channel]['dN']
        dN_tmp_err=result_dict[source][channel]['dN_err']
        v2_tmp=result_dict[source][channel]['v2']

        pT=pT_tmp
        dN=dN_tmp+np.exp(log_dN_above_interp(pT))
        dN_err=dN_tmp_err+np.exp(log_dN_above_err_interp(pT))
        v2=(v2_tmp*dN_tmp+np.exp(log_dN_above_interp(pT))*v2_above_interp(pT))/dN
        v1=np.zeros_like(v2)
        v3=np.zeros_like(v2)
        v4=np.zeros_like(v2)
        v5=np.zeros_like(v2)
        v6=np.zeros_like(v2)


        np.savetxt(os.path.join(destination_dir,"average_sp_"+source+"_"+channel+".dat"),np.transpose(np.concatenate(([pT],[dN],[v1],[v2],[v3],[v4],[v5],[v6]))))



#print(result_dict)

exit(1)


# Hydro
raw=np.loadtxt("results/photons_above_Tfr_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_above_Tfr, v1_above_Tfr, v2_above_Tfr, *rest = raw.T

raw=np.loadtxt("results/tot_photons_T140-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_140_150_tot, v1_music_140_150_tot, v2_music_140_150_tot, *rest = raw.T

raw=np.loadtxt("results/22_photons_T140-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_140_150_22, v1_music_140_150_22, v2_music_140_150_22, *rest = raw.T



####################################################
############## Systems & centralities ##############
####################################################

system_list=["AuAu200"]

cent_class_list_calc=["C10-20"]

additional_cent_class_list=[]

cent_class_list=cent_class_list_calc+additional_cent_class_list


####################################################
############## Systems & centralities ##############
####################################################

def make_destination_dir(tmp_dir):

    if (os.path.isdir(tmp_dir)):
        print("Destination directory ",tmp_dir, " already exists... Aborting.")
        #exit(1)
    else:
        os.makedirs(tmp_dir)


# Loop over photon channel combinations specified in 'extract_dict'
#for result_name, file_function_list in extract_dict.items():
for result_name in rate_dict.keys():

    for system in system_list:

        pre_event_list_dict={}

        ###############################################################################################
        ############### First make a list of events available for each centrality class ###############
        ###############################################################################################
        for cent_class in cent_class_list_calc:

            # Find all events
            #tmp_ref_dir=os.path.dirname(os.path.dirname(os.path.dirname(get_rate_filelist(result_name,system,cent_class,"1")[0])))
            tmp_ref_dir=os.path.join("../raw_hydro_calcs/",system,cent_class) 
            all_file_in_local_dir=os.listdir(path=tmp_ref_dir)
            subdir_regex = re.compile('([0-9]+)')

            event_list=[]
            for tmp_file in all_file_in_local_dir:

                if (not os.path.isdir(os.path.join(tmp_ref_dir,tmp_file))):
                    continue

                match=subdir_regex.match(tmp_file)
                if (match != None):
                    event=int(float(match.group(1)))
                    filelist=get_rate_filelist(result_name,system,cent_class,event)
                    #filelist=[]
                    #for fct_name in file_function_list:
                    #        filelist+=fct_name(system,cent_class,str(event))
#                    filelist=get_kompost_photons_path(system,cent_class,str(event))
#                    filelist+=get_thermal_photons_path(system,cent_class,str(event))

                    #print(filelist)

                    file_exists=[os.path.isfile(filepath) for filepath in filelist]

                    hadron_Qns_path=get_hadron_Qns_path(system,cent_class,str(event))

                    if (all(file_exists)): 
                        if (os.path.isfile(hadron_Qns_path)):
                            event_list.append((cent_class,event))
                        else:
                            print("No hadron Q_s's in ",hadron_Qns_path, "... Will skip the event, but be careful about this...")
                    else:
                        print("No photon in directory ",os.path.join(tmp_ref_dir,tmp_file))
                        print(filelist)
                        print(file_exists)
                        #exit(1)

            pre_event_list_dict[cent_class]=event_list


        ##########################################################################################################
        ############### Second, determine which event should be averaged for each centrality class ###############
        ##########################################################################################################

        event_list_dict={}
        for cent_class in cent_class_list:

            #
            if (cent_class in cent_class_list_calc):
                event_list_dict[cent_class]=pre_event_list_dict[cent_class]
            else:
                # Figure out which centralities to combine
                cent_class_combine=cent_class_combination_info[cent_class]

                #sub_cent_class_dict={}
                #num_events_per_cent_class=[]
                min_event_per_cent_percent=np.inf
                for sub_cent_class in cent_class_combine:
                    #sub_cent_class_dict[sub_cent_class]={}
                    # Figure out the weight
                    tmp_weight=centrality_class_weight(sub_cent_class)
                    #sub_cent_class_dict[sub_cent_class]['weight']=tmp_num
                    tmp_num_events=len(pre_event_list_dict[sub_cent_class])
                    tmp_min_event=tmp_num_events*1.0/tmp_weight
#                    min_event_per_cent_percent=np.min(min_event_per_cent_percent,tmp_min_event)
                    if (tmp_min_event < min_event_per_cent_percent):
                        min_event_per_cent_percent=tmp_min_event

                tmp_event_list=[]
                for sub_cent_class in cent_class_combine:
                    tmp_weight=centrality_class_weight(sub_cent_class)
                    num_event_to_take=int(min_event_per_cent_percent*tmp_weight)
                    #print("pre-batard",sub_cent_class,pre_event_list_dict[sub_cent_class],pre_event_list_dict[sub_cent_class][:num_event_to_take])
                    tmp_event_list=tmp_event_list+pre_event_list_dict[sub_cent_class][:num_event_to_take]
                    
                event_list_dict[cent_class]=tmp_event_list
                #print("batard",cent_class,tmp_event_list)

                #exit(1)

        
##            print(cent_class)
#        print(event_list_dict.keys())
#        #print(event_list_dict)
#        print("miaw")
#        print(event_list_dict['C0-20'])
                   

        for cent_class_label in cent_class_list:
           
            event_list=event_list_dict[cent_class_label]

            #print(event_list)
            
            num_events=len(event_list)

            print("Averaging ",str(num_events)," events for "+system+" "+cent_class_label)

            #print("event_list", event_list)

            if (num_events < 1):
                continue


            res_dict={
                    'pT':None,
                    'yield':None,
                    'v1':None,
                    'v2':None,
                    'v3':None,
                    'v4':None,
                    'v5':None,
                    'v6':None,
            }


            #################################################
            ############## Average over events ##############
            #################################################

            # Read one of the photon files to figure out the size of all the arrays once and for all
            tmp_cent, tmp_ev = event_list[0]
            filename=get_rate_filelist(result_name,system,tmp_cent,str(tmp_ev))[0]
            tmp_res=np.loadtxt(filename)
            NpT, Ncol= tmp_res.shape
            N_harmonics=int((Ncol-2)/2)

            pT_list=tmp_res[:,0]
            photon_event_vn=np.zeros((N_harmonics,NpT))
            photon_event_Psin=np.zeros((N_harmonics,NpT))

            photon_yield=np.zeros((1,NpT))
            photon_vn_rms=np.zeros((N_harmonics,NpT))
            photon_vn_sp=np.zeros((N_harmonics,NpT))
            photon_vn_sp_num=np.zeros((N_harmonics,NpT))
            photon_vn_sp_denum=np.zeros((N_harmonics,NpT))
            photon_cos_psis=np.zeros((N_harmonics,NpT))

#for result_name, file_function_list in extract_dict.items():
#
#    for system in system_list:
#
#        for cent_class in cent_class_list_calc:
#
            #################################################################################
            ############## Average calculations over all existing hydro events ##############
            #################################################################################
            # For each event
            for cent_class, event in event_list:

                # The photon calculations are arranged such that one can simply
                # sum over the files containing each channel's results to
                # combine the different photon production channels together
                file_list=get_rate_filelist(result_name,system,cent_class,str(event))
                #file_list=[]
                #for fct_name in file_function_list:
                #        file_list+=fct_name(system,cent_class,str(event))

                # Sum over all channels
                filename=file_list[0] 
                result=np.loadtxt(filename)
            ##    pT =  result[:,0]
            ##    print(pT)
                for photon_file in file_list[1:]:
                    filename=photon_file 
                    #tpT,ty,tyv1c,tyv1s,tyv2c,tyv2s,tyv3c,tyv3s,tyv4c,tyv4s,tyv5c,tyv5s,tyv6c,tyv6s = np.transpose(np.loadtxt(filename))
                    result+=np.loadtxt(filename)

                tpT, y, yv1c, yv1s, yv2c, yv2s, yv3c, yv3s, yv4c, yv4s, yv5c, yv5s, yv6c, yv6s = np.transpose(result)

                yvn_array=[
                        [1, yv1c, yv1s],
                        [2, yv2c, yv2s],
                        [3, yv3c, yv3s],
                        [4, yv4c, yv4s],
                        [5, yv5c, yv5s],
                        [6, yv6c, yv6s]
                    ]

                # This computes the RMS v_n
                for n, yc, ys in yvn_array:
                    photon_event_vn[n-1,:]=np.sqrt((yc*yc+ys*ys)/(y*y))
                    photon_event_Psin[n-1,:]=np.arctan2(ys,yc)/n

#                print(np.cos(2*photon_event_Psin))

                ####################################################
                ############## Get the hadronic Q_n's ##############
                ####################################################
                # Current hadron Qn format:
                # n  Qn_real  Qn_imag
                n, Qn_real, Qn_im=np.loadtxt(get_hadron_Qns_path(system,cent_class,str(event))).T
                #Qn_real=np.float(Qn_real)
                #Qn_im=np.float(Qn_im)
                Psin_hadrons=np.arctan2(Qn_im, Qn_real)/n
                vn_hadrons=np.zeros_like(Psin_hadrons)+1.0
                #vn_hadrons=Qns_raw[1:,5]
                #Psin_hadrons=Qns_raw[1:,6]

#                print(np.cos(2*Psin_hadrons))

#                print(vn_hadrons[1],photon_event_vn[1,0])
#                print(Psin_hadrons[1],photon_event_Psin[1,0])

#                exit(1)

                ################################################################
                ############## Compute photon average over events ##############
                ################################################################

                # Yield is always just a sum over events
                photon_yield+=y

                # Compute v_n with different definitions
                for n, yc, ys in yvn_array:
                    # This computes the RMS v_n
                    photon_vn_rms[n-1,:]+=np.power(photon_event_vn[n-1,:],2)
                    # This computes the scalar product v_n
                    photon_vn_sp_num[n-1,:]+=photon_event_vn[n-1,:]*vn_hadrons[n-1]*np.cos(n*(photon_event_Psin[n-1,:]-Psin_hadrons[n-1]))
                    photon_vn_sp_denum[n-1,:]+=np.power(vn_hadrons[n-1],2)
                    #photon_vn_sp_num[n-1,:]+=np.cos(n*(photon_event_Psin[n-1,:]-Psin_hadrons[n-1]))
                    #photon_vn_sp_denum[n-1,:]+=1
                    #photon_vn_sp_num[n-1,:]+=photon_event_vn[n-1,:]*photon_event_vn[n-1,:]*np.cos(n*(photon_event_Psin[n-1,:]-photon_event_Psin[n-1,:]))
                    #photon_vn_sp_denum[n-1,:]+=np.power(photon_event_vn[n-1,:],2)
                    photon_cos_psis[n-1,:]+=np.cos(n*(photon_event_Psin[n-1,:]-Psin_hadrons[n-1]))


            # Post processing
            num_events=len(event_list)
            photon_yield/=num_events
            # For RMS v_n
            photon_vn_rms=np.sqrt(photon_vn_rms/num_events)
            # For scalar product v_n
            photon_vn_sp=(photon_vn_sp_num/num_events)/np.sqrt(photon_vn_sp_denum/num_events)
            # For <cos(n(Psi_n^h-Psi_n^g(p_T)))>
            photon_cos_psis=photon_cos_psis/num_events

            #print(pT_list)
            #print(photon_yield)
            #print(photon_vn)

            destination_dir=os.path.join(".","results",result_name,system,cent_class_label)

            make_destination_dir(destination_dir)

            np.savetxt(os.path.join(destination_dir,"average_rms.dat"),np.transpose(np.concatenate(([pT_list],photon_yield,photon_vn_rms))))
            np.savetxt(os.path.join(destination_dir,"average_sp.dat"),np.transpose(np.concatenate(([pT_list],photon_yield,photon_vn_sp))))
            np.savetxt(os.path.join(destination_dir,"average_cosnspsis.dat"),np.transpose(np.concatenate(([pT_list],photon_yield,photon_cos_psis))))
