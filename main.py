import extract as ex


def preprocess():
    #sugesstion kw
    suggdir = 'dataset/sugesstion'
    suggfiles = ex.genFilePath(suggdir)
    output = 'sugesstion_combined'
    output, _ = ex.combineCSV(suggfiles,output)
    ex.add_priority(output,1)

    #relevant kw
    reldir = 'dataset/relevant'
    relfiles = ex.genFilePath(reldir)
    output = 'relevant_combined'
    output, _ = ex.combineCSV(relfiles,output)
    ex.add_priority(output,2)

    #preposition kw
    prepodir = 'dataset/preposition'
    prepofiles = ex.genFilePath(prepodir)
    output = 'preposition_combined'
    output, _ = ex.combineCSV(prepofiles,output)
    ex.add_priority(output,3)

def finalcomb():
    #combining all
    eachouts ='outputs/csv'
    files = ex.genFilePath(eachouts) 
    return ex.combineCSV(files,'final')

preprocess()
file, _ = finalcomb()
file = 'outputs/csv/final.csv'
ex.filter_search_volume(file)
file='outputs/csv/modvol.csv'
ex.keywords_to_txt(file,'kw')