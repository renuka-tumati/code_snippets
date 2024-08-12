# write a python script to auto update .databrickscfg file for multiple profiles

import configparser

def update_cluster_id(config_file, profile_cluster_map):
    # Read the existing .databrickscfg file
    config = configparser.ConfigParser()
    config.read(config_file)

    # Update the cluster ID for each profile
    for profile, cluster_id in profile_cluster_map.items():
        if profile in config:
            config[profile]['cluster_id'] = cluster_id
        else:
            print(f"Profile '{profile}' not found in the configuration file.")

    # Write the updated configuration back to the file
    with open(config_file, 'w') as configfile:
        config.write(configfile)
    print("Cluster IDs updated successfully.")

# Example usage
config_file = '/path/to/.databrickscfg'
profile_cluster_map = {
    'profile1': 'new_cluster_id_1',
    'profile2': 'new_cluster_id_2',
    'profile3': 'new_cluster_id_3'
}

update_cluster_id(config_file, profile_cluster_map)
