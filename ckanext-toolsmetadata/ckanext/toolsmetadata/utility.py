
import ckan.model as model
import ckan.logic.validators as validators
import ckan.lib.navl.dictization_functions as df
from ckan.common import _
import ast
import pprint

# This function reads a text file and passes each line to an array
# Used to read vocabular tags
def getArrayFromFile(filename):
    try:
        dataFile = open(filename,"r")
        dataArray = []
        for data in dataFile:
            dataArray.append( data.replace("\n","") )
        dataFile.close()
        return dataArray
    except Exception as e:
        return []

#This fuction removes unhandled characters from the list of tags
def fixTag(tag):
    res = tag
    res = res.replace(",","_")
    res = res.replace("'","")
    res = res.replace('"',"")
    res = res.replace('(',"")
    res = res.replace(')',"")

    return res

#This function is like CKAN conver to tags but handles many tags
def convertToTags(vocab,newtag,data,error,context):

    new_tags = newtag

    if not new_tags:
        return
    if isinstance(new_tags, basestring):
        new_tags = [new_tags]

    # get current number of tags
    n = 0
    for k in data.keys():
        if k[0] == 'tags':
            n = max(n, k[1] + 1)

    v = model.Vocabulary.get(vocab)
    if not v:
        raise df.Invalid(_('Tag vocabulary "%s" does not exist') % vocab)
    context['vocabulary'] = v

    for tag in new_tags:
        validators.tag_in_vocabulary_validator(tag, context)

    for num, tag in enumerate(new_tags):
        data[('tags', num + n, 'name')] = tag
        data[('tags', num + n, 'vocabulary_id')] = v.id


# Separate a string of tags into individual tags using separator and then adds each tag using convertToTags
# This is neccesary for storing tags as vocabularies that are multiple
def stringToTags(key,data,error,context):

    tag_string = data.get(key)

    vocab = "None"
    separator = ","

    #Multiple tag Vocabularies


    if key[0] == "tool_subjects":
        vocab = "ILRI_vocsubjects"

    if key[0] == "tool_themes":
        vocab = "ILRI_vocthemes"

    if key[0] == "tool_formats":
        vocab = "ILRI_vocformats"

    if key[0] == "tool_datatypes":
        vocab = "ILRI_vocdatatypes"


    #At a certain point in the creation of the dataset tagString is an array. So we test for it
    if type(tag_string) is list:
        tags = tag_string;
    else:
        tags = tag_string.split(separator)


    if vocab == "None":
        raise df.Invalid(_('Tag vocabulary for key "%s" does not exist') % key[0])

    for tag in tags:
        convertToTags(vocab,fixTag(tag),data,error,context)

def loadArray(arrayType):
    if arrayType == 1:
        return getArrayFromFile("/opt/ilri-tools/src/ckanext-toolsmetadata/ckanext/toolsmetadata/lists/subjects.txt")
    if arrayType == 2:
        return getArrayFromFile("/opt/ilri-tools/src/ckanext-toolsmetadata/ckanext/toolsmetadata/lists/thematic_areas.txt")
    if arrayType == 3:
        return getArrayFromFile("/opt/ilri-tools/src/ckanext-toolsmetadata/ckanext/toolsmetadata/lists/formats.txt")
    if arrayType == 4:
        return getArrayFromFile("/opt/ilri-tools/src/ckanext-toolsmetadata/ckanext/toolsmetadata/lists/datatype.txt")
    if arrayType == 5:
        return getArrayFromFile("/opt/ilri-tools/src/ckanext-toolsmetadata/ckanext/toolsmetadata/lists/methods.txt")
    if arrayType == 6:
        return getArrayFromFile("/opt/ilri-tools/src/ckanext-toolsmetadata/ckanext/toolsmetadata/lists/audiance.txt")
    if arrayType == 7:
        return getArrayFromFile("/opt/ilri-tools/src/ckanext-toolsmetadata/ckanext/toolsmetadata/lists/cycle.txt")
    if arrayType == 8:
        return getArrayFromFile("/opt/ilri-tools/src/ckanext-toolsmetadata/ckanext/toolsmetadata/lists/gender.txt")
    if arrayType == 9:
        return getArrayFromFile("/opt/ilri-tools/src/ckanext-toolsmetadata/ckanext/toolsmetadata/lists/spatype.txt")
    if arrayType == 10:
        return getArrayFromFile("/opt/ilri-tools/src/ckanext-toolsmetadata/ckanext/toolsmetadata/lists/datasource.txt")
    if arrayType == 11:
        return getArrayFromFile("/opt/ilri-tools/src/ckanext-toolsmetadata/ckanext/toolsmetadata/lists/outtype.txt")
    if arrayType == 12:
        return getArrayFromFile("/opt/ilri-tools/src/ckanext-toolsmetadata/ckanext/toolsmetadata/lists/assesstype.txt")
    if arrayType == 13:
        return getArrayFromFile("/opt/ilri-tools/src/ckanext-toolsmetadata/ckanext/toolsmetadata/lists/orglevels.txt")
    return []

def valueInArray(value,array):
    try:
        if array.index(value) >= 0:
            return True
        else:
            return False
    except:
        return False

def valueInComaString(value,comaString):
    try:
        array = []
        tarray = comaString.split(",")
        #Values comes with funny characters.. Removing them
        for val in tarray:
            str = val.replace("{","")
            str = str.replace("}","")
            str = str.replace('"',"")
            if str != "":
                array.append(str)
        if array.index(value) >= 0:
            return True
        else:
            return False
    except:
        return False

def comaToArray(comaString):
    try:
        array = []
        tarray = comaString.split(",")
        #Values comes with funny characters.. Removing them
        for val in tarray:
            str = val.replace("{","")
            str = str.replace("}","")
            str = str.replace('"',"")
            if str != "":
                array.append(str)
        return array
    except:
        return []