import json
import sys
import os

'''
=== TO DO===
1. [ ] Replace sys.argv with better flag handling.
2. [ ] Merge the two mark_contracts() functions into one.
3. [ ] Add a try/except block to handle missing or corrupted JSON files.
4. [ ] Create a single helper function for printing the status.
5. [ ] Add a --help flag that explains how to use -t, -i, and -as.
'''

def print_title(DATA_JSON_DIR, title_flags, *titles):
    with open(DATA_JSON_DIR) as f:
        data = json.load(f)
        if title_flags == None:
            for key in data:
                print(">", key)
                for k in data[key]:
                    for l in k:
                        print("-", l, ":",  "Completed" if k[l] == 1  else "Not Complete" )
        elif title_flags == '-t':
            for key in data:
                if key in titles[0]:
                    print(">", key)
                    for k in data[key]:
                        for l in k:
                            print("-", l, ":",  "Completed" if k[l] == 1  else "Not Complete" )
     
def add_new_title(DATA_JSON_DIR, newtitle, item_flags, *items):
    with open(DATA_JSON_DIR) as f:
        data = json.load(f)
        if newtitle in data:
            with open(DATA_JSON_DIR, "w") as f:
                    if not data[newtitle]:
                        new_items = []
                    else:
                        new_items = data[newtitle]
                    if item_flags == '-i':
                        for item in items[0]:
                            item = {item: 0}
                            new_items.append(item)

                    data[newtitle] = new_items
                    json.dump(data, f)
        else:
            with open(DATA_JSON_DIR, "w") as f:
                new_items = []

                if item_flags == '-i':
                    for item in items[0]:
                        item = {item: 0}
                        new_items.append(item)

                data[newtitle] = new_items
                json.dump(data, f)

def del_title(DATA_JSON_DIR, deltitle, item_flags, *items):
    with open(DATA_JSON_DIR, "r") as f:
        data = json.load(f)
        if deltitle in data: 
            if item_flags == None: 
                del data[deltitle]
            else:
                for ifl in items[0]:
                    for i in data[deltitle]:
                        if ifl in i.keys():
                            data[deltitle].remove(i)
            with open(DATA_JSON_DIR, "w") as f:
                json.dump(data, f)

def mark_contracts(DATA_JSON_DIR, titles, set):
    with open(DATA_JSON_DIR, "r") as f:
        data = json.load(f)
        for title in titles:
            if title in data:
                for item in data[title]:
                    for it in item:
                        item[it] = int(set)
        with open(DATA_JSON_DIR, "w") as f:
                json.dump(data, f)

def mark_contracts(DATA_JSON_DIR, titles, set, items):
    with open(DATA_JSON_DIR, "r") as f:
        data = json.load(f)
        for title in titles:
            if title in data:
                for item in data[title]:
                    for it in item:
                        if it in items:
                            item[it] = int(set)
        with open(DATA_JSON_DIR, "w") as f:
                json.dump(data, f)

def main():
    CUR_DIR = os.getcwd()
    DATA_DIR = os.path.join(CUR_DIR, "data")
    DATA_JSON_DIR = os.path.join(CUR_DIR, "data", "data.json")

    if not os.path.isdir(DATA_DIR):
        os.mkdir(DATA_DIR)

    if not os.path.exists(DATA_JSON_DIR):
        with open(DATA_JSON_DIR, "w") as f:
            blank = {}
            json.dump(blank, f)

    args = sys.argv[1:]
    for arg in args:
        if arg == "show": 
            if len(args) > 2:
                title_flags = args[1]
                titles = args[2:]
                print_title(DATA_JSON_DIR, title_flags, titles)
            else:
                titles = None
                title_flags = None
                print_title(DATA_JSON_DIR, title_flags, titles)
        elif arg == "add":
            newtitle = args[1]
            if len(args) > 3:
                item_flags = args[2]
            else:
                item_flags = None
            items = args[3:]
            add_new_title(DATA_JSON_DIR, newtitle, item_flags, items)
        elif arg == "del":
            if len(args) > 3:
                deltitle = args[1]
                item_flags = args[2]
                items = args[3:]
                del_title(DATA_JSON_DIR, deltitle, item_flags, items)
            elif len(args) == 2:
                deltitle = args[1]
                item_flags = None
                items = None
                del_title(DATA_JSON_DIR, deltitle, item_flags, items)

        elif arg == "mark":
            #print(len(args), args)
            if (len(args) > 1):
                t_flag = args[1]
                try:
                    as_index = args.index('-as')
                    try:
                        i_index = args.index('-i')
                        titles = args[2:i_index]
                        items = args[i_index +1 : as_index]
                        mark_contracts(DATA_JSON_DIR, titles, args[as_index + 1], items)
                    except:
                        titles = args[2:as_index]
                        mark_contracts(DATA_JSON_DIR, titles, args[as_index + 1])
                except:
                    return

if __name__ == "__main__":
    main()

