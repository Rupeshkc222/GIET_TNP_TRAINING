'''4.A teacher is conducting a camp for a group of five children. Based on their performance and behavior during the camp, the
 teacher rewards them with chocolates.
Write a Python function to Find the total number of chocolates received by all the children put together.
Assume that each child is identified by an id and it is stored in a tuple and the number of chocolates given to each child is stored in a list.
The teacher also rewards a child with few extra chocolates for his/her best conduct during the camp.
If the number of extra chocolates is less than 1, an error message "Extra chocolates is less than 1", should bedisplayed.
If the given child Id is invalid, an error message "Child id is invalid" should be displayed. Otherwise,the extra chocolates
provided for the child must be added to his/her existing number of chocolates and display the list containing the
total number of chocolates received by each child.


child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

functions

calculate_total_chocolates()

reward_child(child_id_rewarded,extra_chocolates)'''

def reward_child(child_id_rewarded, extra_chocolates, child_id, chocolates_received):
    if extra_chocolates < 1:
        print("Extra chocolates is less than 1")
    elif child_id_rewarded not in child_id:
        print("Child id is invalid")
    else:
        index = child_id.index(child_id_rewarded)
        chocolates_received[index] += extra_chocolates
        print("the final chocolate",chocolates_received)
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]
s=sum(chocolates_received)
c_reward=10
extra_c=2
reward_child(c_reward,extra_c,child_id,chocolates_received)




















