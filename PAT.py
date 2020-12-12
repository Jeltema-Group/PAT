
'''
XPAT - A tool to obtain computed statistical values for images within catalogue files using dmstat.

XPAT is an extension to the MATCha pipleline.
'''
import numpy as np
from astropy.table import Table
from astropy.io import fits
import pandas as pd
import os
import sys
from ciao_contrib.runtool import dmstat

def fit_to_pandas(catalog):
    """
    Converts FITS table to pandas DataFrame.
    
    """
    
    Cat = Table.read(catalog)
    
    df = Cat.to_pandas()
    
    df = df.loc[:,['Name', 'Obsids']]
    
    df['Name'] = df['Name'].str.decode('ASCII') 
    df['Obsids'] = df['Obsids'].str.decode('ASCII') 
    
    list_of = []
    for obs in df['Obsids']:
        obs = obs.split(",")
        list_of.append(obs)
        
    #print(list_of)
    
    df['New_col'] = list_of
    
    #df_obsid.drop('New_Obsid', axis=1, inplace=True)
    
    df.drop('Obsids', axis=1, inplace=True)
    
    df.rename(columns={'New_col':'Obsid'}, inplace=True)
    
    return df

def r500_source(dataframe):
    """ 
    Used to calculate statistics on r500 source region files
        and output pandas DataFrame with stat values. 
    """
    df = dataframe
    
    #empty list
    cat_obs_list = []
    min_list = []
    max_list = []
    mean_list = []
    sigma_list = []
    good_list = []
    null_list = []
    median_list = []
    
    for cat, obs in zip(df['Name'], df['Obsid']):
        for e in obs[:]:
            if os.path.exists("/data1/devon/y3a2/current/observations/{}/I/flux_band1_thresh.expmap".format(e)
                             ) == True:
                if os.path.exists("/data1/devon/y3a2/current/clusters/{}/region_{}_r500_source.reg".format(cat,e)
                                 ) == True:
                    
                    # set v=0 to disbale dmstat display
                    Stats=dmstat("/data1/devon/y3a2/current/observations/{}/I/flux_band1_thresh.expmap["\
                    "sky=region(/data1/devon/y3a2/current/clusters/{}/region_{}_r500_source.reg)]".format(e,cat,e),
                                 centroid=False,
                                 median=True,
                                 sigma=True
                                )
                    # Output parameters using toolname.parametername format
                    median = dmstat.out_median
                    minimum = dmstat.out_min
                    maximum = dmstat.out_max
                    mean = dmstat.out_mean 
                    sigma = dmstat.out_sigma
                    columns = dmstat.out_columns
                    good = dmstat.out_good
                    null = dmstat.out_null
                    
                    #Remove Stats comment to print default screen output or
                    #Remove comments on print statements to output similar format
                    
                    #print("{} / region_{}_r500_source.reg".format(cat, e))
                    #print(Stats)
                    #print("{}".format(columns))                     
                    #print("Median = {}".format(median))                     
                    #print("Minimum = {}".format(minimum))                    
                    #print("Maximum = {}".format(maximum))                    
                    #print("Mean = {}".format(mean))                    
                    #print("Sigma = {}".format(sigma))                    
                    #print("Number of Good Values = {}".format(good))                    
                    #print("Number of Null Values = {}".format(null))                    
                    #print(end="\n")
                    
                    min_list.append(minimum)
                    max_list.append(maximum)
                    mean_list.append(mean)
                    sigma_list.append(sigma)
                    good_list.append(good)
                    null_list.append(null)
                    median_list.append(median)
                    cat_obs_list.append((cat,e))
                    
            else:
                pass
            
    # Create empty DataFrame
    df_r500_src = pd.DataFrame()
    
    df_r500_src["Catalog"] = pd.Series(cat_obs_list)
    df_r500_src["Minimum"] = pd.Series(min_list)
    df_r500_src["Maximum"] = pd.Series(max_list)
    df_r500_src["Mean"] = pd.Series(mean_list)
    df_r500_src["Sigma"] = pd.Series(sigma_list)
    df_r500_src["Good"] = pd.Series(good_list)
    df_r500_src["Null"] = pd.Series(null_list)
    df_r500_src["Median"] = pd.Series(median_list)
    
    return df_r500_src

def r2500_source(dataframe):
    """ 
    Used to calculate statistics on r2500 source region files
         and output pandas DataFrame with stat values. 
    """
    
    df = dataframe
    
    #empty list
    cat_obs_list = []
    min_list = []
    max_list = []
    mean_list = []
    sigma_list = []
    good_list = []
    null_list = []
    median_list = []
    
    for cat, obs in zip(df_obsid['Name'], df_obsid['Obsid']):
        for e in obs[:]:
            if os.path.exists("/data1/devon/y3a2/current/observations/{}/I/flux_band1_thresh.expmap".format(e)
                             ) == True:
                if os.path.exists("/data1/devon/y3a2/current/clusters/{}/region_{}_r2500_source.reg".format(cat,e)
                                 ) == True:
                    
                    # set v=0 to disbale dmstat display
                    Stats=dmstat("/data1/devon/y3a2/current/observations/{}/I/flux_band1_thresh.expmap["\
                    "sky=region(/data1/devon/y3a2/current/clusters/{}/region_{}_r2500_source.reg)]".format(e,cat,e),
                                 centroid=False,
                                 median=True,
                                 sigma=True
                                )
                    # Output parameters using toolname.parametername format
                    median = dmstat.out_median
                    minimum = dmstat.out_min
                    maximum = dmstat.out_max
                    mean = dmstat.out_mean 
                    sigma = dmstat.out_sigma
                    columns = dmstat.out_columns
                    good = dmstat.out_good
                    null = dmstat.out_null
                    
                    #Remove Stats comment to print default screen output or
                    #Remove comments on print statements to output similar format
                    
                    #print("{} / region_{}_r2500_source.reg".format(cat, e))
                    #print(Stats)
                    #print("{}".format(columns))                     
                    #print("Median = {}".format(median))                     
                    #print("Minimum = {}".format(minimum))                    
                    #print("Maximum = {}".format(maximum))                    
                    #print("Mean = {}".format(mean))                    
                    #print("Sigma = {}".format(sigma))                    
                    #print("Number of Good Values = {}".format(good))                    
                    #print("Number of Null Values = {}".format(null))                    
                    #print(end="\n")
                    
                    min_list.append(minimum)
                    max_list.append(maximum)
                    mean_list.append(mean)
                    sigma_list.append(sigma)
                    good_list.append(good)
                    null_list.append(null)
                    median_list.append(median)
                    cat_obs_list.append((cat,e))
            else:
                pass
            
    # Create empty DataFrame
    df_r2500_src = pd.DataFrame()
    
    df_r2500_src["Catalog"] = pd.Series(cat_obs_list)
    df_r2500_src["Minimum"] = pd.Series(min_list)
    df_r2500_src["Maximum"] = pd.Series(max_list)
    df_r2500_src["Mean"] = pd.Series(mean_list)
    df_r2500_src["Sigma"] = pd.Series(sigma_list)
    df_r2500_src["Good"] = pd.Series(good_list)
    df_r2500_src["Null"] = pd.Series(null_list)
    df_r2500_src["Median"] = pd.Series(median_list)
            
    return df_r2500_src

def _500_kiloparsecs_source(dataframe):
    """ 
    Used to calculate statistics on 500_kiloparsecs source region files
        and output pandas DataFrame with stat values. 
    """
    
    df = dataframe
    
    #empty list
    cat_obs_list = []
    min_list = []
    max_list = []
    mean_list = []
    sigma_list = []
    good_list = []
    null_list = []
    median_list = []
    
    for cat, obs in zip(df['Name'], df['Obsid']):
        for e in obs[:]:
            if os.path.exists("/data1/devon/y3a2/current/observations/{}/I/flux_band1_thresh.expmap".format(e)
                             ) == True:
                if os.path.exists("/data1/devon/y3a2/current/clusters/{}/region_{}_500_kiloparsecs_source.reg".format(cat,e)
                                 ) == True:
                    
                    # set v=0 to disbale dmstat display
                    Stats=dmstat("/data1/devon/y3a2/current/observations/{}/I/flux_band1_thresh.expmap["\
                    "sky=region(/data1/devon/y3a2/current/clusters/{}/region_{}_500_kiloparsecs_source.reg)]".format(e,cat,e),
                                 centroid=False,
                                 median=True,
                                 sigma=True
                                )
                    # Output parameters using toolname.parametername format
                    median = dmstat.out_median
                    minimum = dmstat.out_min
                    maximum = dmstat.out_max
                    mean = dmstat.out_mean 
                    sigma = dmstat.out_sigma
                    columns = dmstat.out_columns
                    good = dmstat.out_good
                    null = dmstat.out_null
                    
                    #Remove Stats comment to print default screen output or
                    #Remove comments on print statements to output similar format
                    
                    #print("{} / region_{}_500_kiloparsecs_source.reg".format(cat, e)) 
                    #print(Stats)
                    #print("{}".format(columns))
                    #print("Median = {}".format(median))                     
                    #print("Minimum = {}".format(minimum))                    
                    #print("Maximum = {}".format(maximum))                    
                    #print("Mean = {}".format(mean))                    
                    #print("Sigma = {}".format(sigma))                    
                    #print("Number of Good Values = {}".format(good))                    
                    #print("Number of Null Values = {}".format(null))                    
                    #print(end="\n")
                    
                    min_list.append(minimum)
                    max_list.append(maximum)
                    mean_list.append(mean)
                    sigma_list.append(sigma)
                    good_list.append(good)
                    null_list.append(null)
                    median_list.append(median)
                    cat_obs_list.append((cat,e))
            else:
                pass
            
    # Create empty DataFrame
    df_500_kilo = pd.DataFrame()
    
    df_500_kilo["Catalog"] = pd.Series(cat_obs_list)
    df_500_kilo["Minimum"] = pd.Series(min_list)
    df_500_kilo["Maximum"] = pd.Series(max_list)
    df_500_kilo["Mean"] = pd.Series(mean_list)
    df_500_kilo["Sigma"] = pd.Series(sigma_list)
    df_500_kilo["Good"] = pd.Series(good_list)
    df_500_kilo["Null"] = pd.Series(null_list)
    df_500_kilo["Median"] = pd.Series(median_list)
            
    return df_500_kilo

def r500_background(dataframe):
    """ 
    Used to calculate statistics on r500_background region files
        and output pandas DataFrame with stat values.
    """
    
    df = dataframe
    
    #empty list
    cat_obs_list = []
    min_list = []
    max_list = []
    mean_list = []
    sigma_list = []
    good_list = []
    null_list = []
    median_list = []
    
    for cat, obs in zip(df['Name'], df['Obsid']):
        for e in obs[:]:
            if os.path.exists("/data1/devon/y3a2/current/observations/{}/I/flux_band1_thresh.expmap".format(e)
                             ) == True:
                if os.path.exists("/data1/devon/y3a2/current/clusters/{}/region_{}_r500_background.reg".format(cat,e)
                                 ) == True:
                    
                    # set v=0 to disbale dmstat display
                    Stats=dmstat("/data1/devon/y3a2/current/observations/{}/I/flux_band1_thresh.expmap["\
                    "sky=region(/data1/devon/y3a2/current/clusters/{}/region_{}_r500_background.reg)]".format(e,cat,e),
                                 centroid=False,
                                 median=True,
                                 sigma=True
                                )
                    # Output parameters using toolname.parametername format
                    median = dmstat.out_median
                    minimum = dmstat.out_min
                    maximum = dmstat.out_max
                    mean = dmstat.out_mean 
                    sigma = dmstat.out_sigma
                    columns = dmstat.out_columns
                    good = dmstat.out_good
                    null = dmstat.out_null
                    
                    #Remove Stats comment to print default screen output or
                    #Remove comments on print statements to output similar format
                    
                    #print("{} / region_{}_500_background.reg".format(cat, e)) 
                    #print(Stats)
                    #print("{}".format(columns))
                    #print("Median = {}".format(median))                     
                    #print("Minimum = {}".format(minimum))                    
                    #print("Maximum = {}".format(maximum))                    
                    #print("Mean = {}".format(mean))                    
                    #print("Sigma = {}".format(sigma))                    
                    #print("Number of Good Values = {}".format(good))                    
                    #print("Number of Null Values = {}".format(null))                    
                    #print(end="\n")
                    
                    min_list.append(minimum)
                    max_list.append(maximum)
                    mean_list.append(mean)
                    sigma_list.append(sigma)
                    good_list.append(good)
                    null_list.append(null)
                    median_list.append(median)
                    cat_obs_list.append((cat,e))
                    
            else:
                pass
            
    # Create empty DataFrame
    df_r500_bckg = pd.DataFrame()
    
    df_r500_bckg["Catalog"] = pd.Series(cat_obs_list)
    df_r500_bckg["Minimum"] = pd.Series(min_list)
    df_r500_bckg["Maximum"] = pd.Series(max_list)
    df_r500_bckg["Mean"] = pd.Series(mean_list)
    df_r500_bckg["Sigma"] = pd.Series(sigma_list)
    df_r500_bckg["Good"] = pd.Series(good_list)
    df_r500_bckg["Null"] = pd.Series(null_list)
    df_r500_bckg["Median"] = pd.Series(median_list)
            
    return df_r500_bckg

def main():
    """
    Main function calls each function and saves DataFrames to CSV files. 
    
    """
    
    catalog = sys.argv[1] #First arguement given by user
    
    dataframe = fit_to_pandas(catalog)
    
    print("\nMaking r500 Source DataFrame...")
    
    df_r500_src = r500_source(dataframe)
    
    print("\ndf_r500_src Created!")
    print("\nMaking r2500 Source DataFrame...")
    
    df_r2500_src = r2500_source(dataframe)
    
    print("\ndf_r2500_src Created!")
    print("\nMaking 500 Kilopasecs DataFrame...")
    
    df_500_kilo = _500_kiloparsecs_source(dataframe)
    
    print("\ndf_500_kilo Created!")
    print("\nMaking r500 Background DataFrame...")    
    
    df_r500_bckg = r500_background(dataframe)
    
    print("\ndf_r500_bckg Created!")
    print("\nSaving DataFrames to CSV files...")
    
    df_r500_src.to_csv(r"/home/jose/r500_source.csv")
    df_r2500_src.to_csv(r"/home/jose/r2500_source.csv")
    df_500_kilo.to_csv(r"/home/jose/500_kilo.csv")
    df_r500_bckg.to_csv(r"/home/jose/r500_bckg.csv")
    
    print("Done!")
    
if __name__ == '__main__':
    main()