from database.db_manager import (create_database ,insert_sample_data,get_all_containers,get_one_container,update_container,delete_container)

# create_database()

rows = insert_sample_data('C1012', 'Loaded', 'Dock 1', 'Reefer')


# delete_container("C1005")
containers = get_all_containers()

# updated_containner = update_container("C1003","Empty")
# onecontainer = get_one_container("C1003")

# print("recod deleted sucessfully")
print(rows)
# print("DB updated sucessfully")
print(containers)
# print(onecontainer)



