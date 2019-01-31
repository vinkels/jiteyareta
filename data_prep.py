import pandas as pd
import matplotlib.pyplot as plt



def data_prep():
    final_dfs = []
    df = pd.read_pickle('pickles/test_nr_hives.p')
    cur_samp = 0
    sample = 0
    for i, row in df.iterrows():
        df_temp = df.at[i, 'step_data']
        df_temp['obstacle_dens'] = row['obstacle_density']
        df_temp['food_dens'] = row['food_density']
        df_temp['n_hives'] = row['nr_hives']
        df_temp['sample'] = row['Run']
        df_temp['step'] = df_temp.index
        sample += 1
        final_dfs.append(df_temp)
    df_final = pd.concat(final_dfs)
    df_final.to_csv('pickles/test_final.csv')
    df_final['s_f'] = 
    df_final['bee_hives'] =
    df_final['death_age'] = 
    df_final['food_bee'] = 
    # df_step = df_final.groupby(['obstacle_dens', 'food_dens', 'n_hives', 'step'])[['HiveFood', 'scout bees']].describe()
    # print(df_step)

if __name__ == "__main__":
    data_prep()


        

    
