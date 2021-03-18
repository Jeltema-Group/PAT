
'''
PAT - A tool to obtain computed statistical values for images within catalogue files using dmstat.

PAT is an extension to the MATCha pipleline.
'''
import numpy as np
from astropy.table import Table
from astropy.io import fits
import pandas as pd
import os
import sys
import yaml
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

def configuration():
    """ Opens and returns config file."""
    with open(r"./Config.yml", 'r') as stream:
        config = yaml.safe_load(stream)

    return config

def create_df(dataframe, config):
    """ 
    Used to calculate statistics on r500 source region files
        and output pandas DataFrame with stat values. 
    """
    df = dataframe
    
    #empty list
    cat_list = []
    obsid_list = []
    min_list = []
    max_list = []
    mean_list = []
    sigma_list = []
    good_list = []
    null_list = []
    median_list = []
    
    for cat_, obsid_ in zip(df['Name'], df['Obsid']):
        for obs_ in obsid_[:]:
            if os.path.exists(config["Path_1"].format(obs_)
                             ) == True:
                if os.path.exists(config["Path_2"].format(cat_,obs_)
                                 ) == True:
                    
                    # set v=0 to disbale dmstat display
                    Stats=dmstat("/data1/devon/y3a2/current/observations/{}/I/flux_band1_thresh.expmap["\
                    "sky=region(/data1/devon/y3a2/current/clusters/{}/region_{}_r500_source.reg)]".format(obs_,cat_,obs_),
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
                    cat_list.append(cat_)
                    obsid_list.append(obs_)
                    
            else:
                pass
            
    # Create empty DataFrame
    df_created = pd.DataFrame()
    
    df_created["Catalog"] = pd.Series(cat_list)
    df_created["Obsid"] = pd.Series(obsid_list)
    df_created["Minimum"] = pd.Series(min_list)
    df_created["Maximum"] = pd.Series(max_list)
    df_created["Mean"] = pd.Series(mean_list)
    df_created["Sigma"] = pd.Series(sigma_list)
    df_created["Good"] = pd.Series(good_list)
    df_created["Null"] = pd.Series(null_list)
    df_created["Median"] = pd.Series(median_list)
    
    return df_created

def main():
    """
    Main function calls each function and saves DataFrames to CSV files. 
    
    """
    
    # First arguement given by user
    catalog = sys.argv[1]

    # Config file
    config = configuration()

    dataframe = fit_to_pandas(catalog)
    
    print("\nMaking DataFrame...")
    
    df_output = create_df(dataframe, config)
    
    print(f"\n Dataframe Created!")
    
    print("\nSaving DataFrame to CSV file...")
    
    df_output.to_csv(r"./{}.csv".format(config["Title"]))
    
    print("Done!")
    
if __name__ == '__main__':
    main()
