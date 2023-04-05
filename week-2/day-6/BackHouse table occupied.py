'''The owner of a BakeHouse wants to keep track of the tables
that are occupied in his cafe. Assume that there are 10 tables in his cafe numbered from 1 to 10. As and when a table is occupied, it must be added to the occupied_table_list and when a customer leaves, the corresponding table must be removed from the list.

BakeHouse
- occupied_table_list
_init_()
+ get_occupied_table_list()
+ allocate_table()
+ deallocate_table(table_number)
Write a python program to implement BakeHouse class.
Represent occupied_table_list using an appropriate data
structure.


Note: Table numbers should be maintained in ascending order in the occupied_table_list.


Tables should be allocated and de-allocated as mentioned in the example below:

Example: Suppose tables 1, 2, 3 and 4 are initially allocated. Now if a new customer arrives, he should be allocated table 5 and the table list should be accordingly updated. If now customer at table 2 leaves, table list should be accordingly updated and the next new customer should be allocated table 2 as it is the first free table.


Implement the allocation logic in allocate_table() method and de-allocation logic in deallocate_table() method.
-------------------------------------------------------
10.Write a python program to reverse a linked list containing
integer data.
Use the LinkedList class and methods in it to implement the
 above program.'''

class BakeHouse:
    def __init__(self):
        self.occupied_table_list = []

    def get_occupied_table_list(self):
        return self.occupied_table_list

    def allocate_table(self):
        for table in range(1, 11):
            if table not in self.occupied_table_list:
                self.occupied_table_list.append(table)
                self.occupied_table_list.sort()
                return table
        return None

    def deallocate_table(self, table_number):
        if table_number in self.occupied_table_list:
            self.occupied_table_list.remove(table_number)
            return True
        return False
bakehouse = BakeHouse()
print("at start restuarent",bakehouse.get_occupied_table_list())

table1 = bakehouse.allocate_table()
table2 = bakehouse.allocate_table()
table3 = bakehouse.allocate_table()
table4 = bakehouse.allocate_table()
print("after allocation of table till table 4",bakehouse.get_occupied_table_list())

table5 = bakehouse.allocate_table()
print("after allocation of table till table 5",bakehouse.get_occupied_table_list())

bakehouse.deallocate_table(2)
print("after the deallocation of the table 2",bakehouse.get_occupied_table_list())
