# -*- coding: utf-8 -*-
"""
@author: Sven Maurice Morlock
@date: 11.10.2021

Provides functions build for kaggle API
-> conda install -c conda-forge kaggle
-> folderpath included <anaconda_path>/lib/python3.8/site-packages/<name>.pth
"""
import os
import zipfile
import shutil
import pandas as pd

def get_kaggle_data(data_name,foldername = '', data_format = '.csv', read_as = str):
    """
    Parameters
    ----------
    data_name : string
        name for dataset according to kaggle api.
    foldername : string, optional
        folder where downloaded data is stored.
    data_format : string, optional
        file type from kaggle set (including leading dot). The default is '.csv'.
    read_as: default type of columns

    Returns
    -------
    dictionary of pd.dataframes. 
    names according to name in kaggle set (including file ending)

    """
    #data_name = 'noaa/hurricane-database'
    #data_format = ".csv"
    bash_command = 'kaggle datasets download -d '+ data_name + " -p 'tmp_data'"
    try:
        os.mkdir('tmp_data')
        os.system(bash_command)
        zip_name = os.listdir('tmp_data')[0]
        zip_names = zipfile.ZipFile('tmp_data' + os.sep + zip_name)
        zip_names = zip_names.namelist()
        zip_names = [name for name in zip_names if name.endswith(data_format) ]
        z = zipfile.ZipFile('tmp_data' + os.sep + zip_name)
        z.extractall('tmp_data'+ os.sep + zip_name[:-4])
        data_dict = {}
        for data_file in zip_names:
            pd_data = pd.read_csv('tmp_data' + os.sep + zip_name[:-4] + os.sep + data_file, dtype = read_as)
            data_dict[data_file] = pd_data
    finally:
        shutil.rmtree('tmp_data')
        print("'tmp_data' folder removed")
    return(data_dict)