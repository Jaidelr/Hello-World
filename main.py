# Task 17: Import the modules csv, tui and visual
# TODO: Your code here
import tui
import visual
import data
from csv import reader
import os

# Task 18: Create an empty list named 'records'.
# This will be used to store the date read from the source data file.
# TODO: Your code here
records=[]
def run():

    # Task 19: Call the function welcome of the module tui.
    # This will display our welcome message when the program is executed.
    # TODO: Your code here
    tui.welcome()
    while True:
        # Task 20: Using the appropriate function in the module tui, display a menu of options
        # for the different operations that can be performed on the data.
        # Assign the selected option to a suitable local variable
        # TODO: Your code here
        o=tui.menu()
        # Task 21: Check if the user selected the option for loading data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data loading
        # operation has started.
        # - Load the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data loading
        # operation has completed.
        #
        # To load the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to retrieve a file path for the CSV data file.  You
        # should appropriately handle the case where this is None.
        # - Read each line from the CSV file and add it to the list 'records'. You should appropriately handle the case
        # where the file cannot be found
        # TODO: Your code here
        if o==1:
            tui.started("Data Loading")
            f_path=tui.source_data_path()
            try:
                with open(f_path,'r') as f:
                    reader_csv=reader(f)
                    for row in reader_csv:
                        records.append(row)
            except:
                print("file does not exist")
            for record in records:
                print(record)
            tui.completed("Data Loading")
        # Task 22: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to display a menu of options for processing the data.
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve an entity then
        #       - Use the appropriate function in the module tui to indicate that the entity retrieval process
        #       has started.
        #       - Use the appropriate function in the module tui to retrieve the entity name
        #       - Find the record for the specified entity in records.  You should appropriately handle the case
        #       where the entity cannot be found.
        #       - Use the appropriate function in the module tui to list the entity
        #       - Use the appropriate function in the module tui to indicate that the entity retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve an entity's details then
        #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
        #       process has started.
        #       - Use the appropriate function in the module tui to retrieve the entity details
        #       - Find the record for the specified entity details in records.  You should appropriately handle the
        #       case where the entity cannot be found.
        #       - Use the appropriate function in the module tui to list the entity
        #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
        #       process has completed.
        #
        #   - If the user selected the option to categorise entities by their type then
        #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
        #       process has started.
        #       - Iterate through each record in records and assemble a dictionary containing a list of planets
        #       and a list of non-planets.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
        #       process has completed.
        #
        #   - If the user selected the option to categorise entities by their gravity then
        #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
        #       process has started.
        #       - Use the appropriate function in the module tui to retrieve a gravity range
        #       - Iterate through each record in records and assemble a dictionary containing lists of entities
        #       grouped into low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
        #       process has completed.
        #
        #   - If the user selected the option to generate an orbit summary then
        #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
        #       started.
        #       - Use the appropriate function in the module tui to retrieve a list of orbited planets.
        #       - Iterate through each record in records and find entities that orbit a planet in the list of
        #       orbited planets.  Assemble the found entities into a nested dictionary such that each entity can be
        #       accessed as follows:
        #           name_of_dict[planet_orbited][category]
        #       where category is "low" if the mean radius of the entity is below 100 and "high" otherwise.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
        #       completed.
        # TODO: Your code here
        if o == 2:
            tui.started("Data Processing")
            pt=tui.process_type()
            # data processing options
            one_line = 0
            if pt==1:
                tui.started("entity retrieval process")
                e_n=tui.entity_name().lower()
                try:
                    for r in records:
                        if str(r[0]).lower()==e_n:
                            #specified record
                            s_r=r
                            break
                        else:
                            one_line+=1
                            if one_line==1:
                                print("")
                except:
                    print("An error occurred/the entity does not exist")
                tui.list_entity(s_r,cols=[])
            tui.completed("entity retrieval process")
            #retrieve the entity's details option

            if pt==2:
                tui.started("Process to retrieve the entity's details")
                #entity details
                e_d=tui.entity_details()
                one_line2=0
                try:
                    for r in records:
                        if str(r[0])==e_d[0]:
                            #specified record
                            s2_r=r
                            break
                        else:
                            one_line2 += 1
                            #prevents printing of unnecessary multiple lines
                            if one_line2 == 1:
                                print("")
                except:
                    print("An error occurred/ the entity does not exist")
                tui.list_entity(s2_r,e_d[1])
                tui.completed("Process to retrieve the entity's details")
                #categorise entities by their type
            if pt==3:
                tui.started("Process to categorise entities by their type")
                planets = []
                non_planets = []
                #print(records)
                for i in records:
                    #print(str(i[1]).lower().strip(' '),"FALSE")
                    if str(i[1]).lower().strip(' ')=="false":
                        #print(str(i[1]).lower())
                        non_planets.append(i[0])
                    if str(i[1]).lower().strip(' ')=="true":
                        planets.append(i[0])
                #print(planets)
                cat={"planets":planets,"non-planets":non_planets}
                tui.list_categories(categories=cat)
                #print(cat["non-planets"])
                print("Planets->",cat["planets"])
                print("Non-Planets->", cat["non-planets"])
                tui.completed("Process to categorise entities by their type")
            #Categorise entities by gravity
            if pt == 4:
                tui.started("Process to Categorise entities by gravity")
                l_m=tui.gravity_range()
                #list of entities
                low=[]
                medium=[]
                high=[]
                records.pop(0)
                for i in records:
                    if float(i[8])>float(l_m[1]):
                        high.append(i[0])
                    if float(i[8])<float(l_m[0]):
                        low.append(i[0])
                    else:
                        medium.append(i[0])
                catgs={"low": low,"medium": medium,"high":high}
                tui.list_categories(categories=catgs)
                print("Low->", catgs["low"])
                print("Medium->",catgs["medium"])
                print("High", catgs["high"])
                tui.completed("Process to Categorise entities by gravity")

            if pt==5:
                tui.started("Process to generate an orbit summary")
                orbt = tui.orbits()
                f_d = {key: {"low": [], "high": []} for key in orbt}
                for j in range(len(orbt)):
                    for i in range(len(records)):
                        # print(records[i][10])
                        if str(orbt[j]).lower().strip(' ') == str(records[i][21]).lower().strip(' '):
                            if float(records[i][10]) < float(100):
                                f_d[str(orbt[j])]["low"].append(str(records[i][0]))
                            else:
                                f_d[str(orbt[j])]["high"].append(str(records[i][0]))
                tui.list_categories(categories=f_d)
                tui.completed("Process to generate an orbit summary")

            '''
            if pt==5:
                tui.started("Process to generate an orbit summary")
                orbt=tui.orbits()

                for i in range(len(orbt)):
                    for j in orbt:
                        j[i]=[]
                    for k in records:
                        if str(j[i]).lower==str(k[22]).lower:
                            l.append(k[0])


                tui.completed("generate an orbit summary")
            '''
        # Task 23: Check if the user selected the option for visualising data.  If so, then do the following:
        # - Use the appropriate function in the module tui to indicate that the data visualisation operation
        # has started.
        # - Visualise the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data visualisation
        # operation has completed.
        #
        # To visualise the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to retrieve the type of visualisation to display.
        # - Check what option has been selected
        #
        #   - if the user selected the option to visualise the entity type then
        #       - Use the appropriate function in the module tui to indicate that the entity type visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing a list of planets and a list of
        #       non-planets.
        #       - Use the appropriate function in the module visual to display a pie chart for the number of planets
        #       and non-planets
        #       - Use the appropriate function in the module tui to indicate that the entity type visualisation
        #       process has completed.
        #
        #   - if the user selected the option to visualise the entity gravity then
        #       - Use the appropriate function in the module tui to indicate that the entity gravity visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
        #       low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module visual to display a bar chart for the gravities
        #       - Use the appropriate function in the module tui to indicate that the entity gravity visualisation
        #       process has completed.

        #   - if the user selected the option to visualise the orbit summary then
        #       - Use the appropriate function in the module tui to indicate that the orbit summary visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a nested dictionary of orbiting planets.
        #       - Use the appropriate function in the module visual to display subplots for the orbits
        #       - Use the appropriate function in the module tui to indicate that the orbit summary visualisation
        #       process has completed.
        #
        #   - if the user selected the option to animate the planet gravities then
        #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
        #       low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module visual to animate the gravity.
        #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
        #       process has completed.
        # TODO: Your code here
        if o==3:
            tui.started("data visualisation operation")
            o_p=tui.visualise()

            if o_p==1:
                tui.started("entity type visualisation process")
                planets = []
                non_planets = []
                # print(records)
                for i in records:
                    # print(str(i[1]).lower().strip(' '),"FALSE")
                    if str(i[1]).lower().strip(' ') == "false":
                        # print(str(i[1]).lower())
                        non_planets.append(i[0])
                    if str(i[1]).lower().strip(' ') == "true":
                        planets.append(i[0])
                # print(planets)
                cat = {"planets": planets, "non-planets": non_planets}
                #print(cat)
                visual.entities_pie(cat)
                tui.completed("entity type visualisation process")

            if o_p==2:
                tui.started("entity gravity visualisation process")
                l_m = tui.gravity_range()
                # list of entities
                low = []
                medium = []
                high = []
                records.pop(0)
                for i in records:
                    if float(i[8]) > float(l_m[1]):
                        high.append(i[0])
                    if float(i[8]) < float(l_m[0]):
                        low.append(i[0])
                    else:
                        medium.append(i[0])
                catgs = {"low": low, "medium": medium, "high": high}
                visual.entities_bar(catgs)
            if o_p==3:
                tui.started("orbit summary visualisation")
                #-----------------------------------
                orbt = tui.orbits()
                f_d = {key: {"low": [], "high": []} for key in orbt}
                for j in range(len(orbt)):
                    for i in range(len(records)):
                        # print(records[i][10])
                        if str(orbt[j]).lower().strip(' ') == str(records[i][21]).lower().strip(' '):
                            if float(records[i][10]) < float(100):
                                f_d[str(orbt[j])]["low"].append(str(records[i][0]))
                            else:
                                f_d[str(orbt[j])]["high"].append(str(records[i][0]))
                visual.orbits(f_d)
                tui.completed("orbit summary visualisation")

            if o_p==4:
                tui.started("gravity animation visualisation process")
                l_m = tui.gravity_range()
                # list of entities
                low = []
                medium = []
                high = []
                records.pop(0)
                for i in records:
                    if float(i[8]) > float(l_m[1]):
                        high.append(i[0])
                    if float(i[8]) < float(l_m[0]):
                        low.append(i[0])
                    else:
                        medium.append(i[0])
                catgs = {"low": low, "medium": medium, "high": high}
                visual.gravity_animation(catgs)
                tui.completed("gravity animation visualisation process")

        # Task 28: Check if the user selected the option for saving data.  If so, then do the following:
        # - Use the appropriate function in the module tui to indicate that the save data operation has started.
        # - Save the data (see below)
        # - Use the appropriate function in the module tui to indicate that the save data operation has completed.
        #
        # To save the data, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create an AbstractWriter class with abstract methods and a concrete
        # Writer class that inherits from the AbstractWriter class.  You should then use this to write the records to
        # a plaintext file using a suitable structure e.g. all the planets followed by non-planets in alphabetical
        # order.
        #
        # TODO: Your code here
        if o==4:
            tui.started("save data operation")
            class AbstractWriter:
                def abstract(self,f):
                    self.f=open("save.txt", 'a')
                    #self.save_data=save_data
            class Writer(AbstractWriter):
                def wwrite(self, data):
                    self.data=data
                    open("save.txt", 'a').write(data)
                pass
            planets=[]
            non_planets=[]
            for i in records:
                # print(str(i[1]).lower().strip(' '),"FALSE")
                if str(i[1]).lower().strip(' ') == "false":
                    # print(str(i[1]).lower())
                    non_planets.append(i[0])
                if str(i[1]).lower().strip(' ') == "true":
                    planets.append(i[0])
                # print(planets)
            planets = sorted(planets)
            non_planets = sorted(non_planets)
            a_z_p=[]
            a_z_n=[]

            for i in planets:
                for j in records:
                    if str(i).lower().strip(' ')==str(j[0]).lower().strip(' '):
                        a_z_p.append(j)
            for nested_list in a_z_p:
                Writer().wwrite('\t'.join(nested_list))
                #print('\t'.join(nested_list))
                for i in non_planets:
                    for j in records:
                        if str(i).lower().strip(' ') == str(j[0]).lower().strip(' '):
                            a_z_n.append(j)
            for nested_list in a_z_n:
                Writer().wwrite('\t'.join(nested_list))
                #print('\t'.join(nested_list))
            print("Data saved in {}".format(os.getcwd()))
            tui.completed("save data operation")
        # Task 29: Check if the user selected the option for exiting.  If so, then do the following:
        # break out of the loop
        # TODO: Your code here
        if o==5:
            break
        # Task 30: If the user selected an invalid option then use the appropriate function of the module tui to
        # display an error message
        # TODO: Your code here
        else:
            tui.error("Option Selected Does Not Exist! Select a valid option")

if __name__ == "__main__":
    run()
