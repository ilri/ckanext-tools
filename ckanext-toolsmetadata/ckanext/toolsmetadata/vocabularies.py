from utility import getArrayFromFile
from utility import fixTag
import ckan.plugins.toolkit as toolkit
import logging

#This function creates a vocabulary if it does not exists and add the tags from a source file.
def createVocabulary(vocID,sourceFile):
    user = toolkit.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    try:
        data = {'id': vocID}
        vocab = toolkit.get_action('vocabulary_show')(context, data)
        logging.info(vocID + " vocabulary already exists. Loading list for update")
        for tag in getArrayFromFile(sourceFile):
            data = {'name': fixTag(tag), 'vocabulary_id': vocab['id']}
            try:
                toolkit.get_action('tag_create')(context, data)
                logging.info("Tag {0} added to vocab '{1}'".format(tag,vocID))
            except Exception as e:
                logging.info(str(e))
                pass

    except toolkit.ObjectNotFound:
        logging.info("Creating vocab '{0}'".format(vocID))
        data = {'name': vocID}
        vocab = toolkit.get_action('vocabulary_create')(context, data)
        try:
            for tag in getArrayFromFile(sourceFile):
                logging.info("Adding tag {0} to vocab '{1}'".format(tag,vocID))
                data = {'name': fixTag(tag), 'vocabulary_id': vocab['id']}
                toolkit.get_action('tag_create')(context, data)
                logging.info("Tag {0} added to vocab '{1}'".format(tag,vocID))
        except Exception as e:
            logging.info(str(e))
            return False
    except Exception as e:
        logging.info(str(e))


    return True

#This fuction removes a vocabulary
def deleteVocab(vocName,vocListFile):

    user = toolkit.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}

    data = {'id': vocName}
    data2 = {'id': vocName}

    for tag in getArrayFromFile(vocListFile):
        data = {'id': fixTag(tag), 'vocabulary_id': vocName}
        try:
            toolkit.get_action('tag_delete')(context, data)
            logging.info("Tag {0} deleted".format(tag))
        except:
            print "Tag " + tag + " Does not exists"


    toolkit.get_action('vocabulary_delete')(context, data2)
    print vocName + " vocabulary deleted."

# This Helper function creates the subjects vocabulary from a text file
def createSubjectsVocab():
    return createVocabulary("ILRI_vocsubjects","/opt/ckan-tools/ckan/src/ckanext-toolsmetadata/ckanext/toolsmetadata/lists/subjects.txt")


# This Helper function creates the themes vocabulary from a text file
def createThemesVocab():
     return createVocabulary("ILRI_vocthemes","/opt/ckan-tools/ckan/src/ckanext-toolsmetadata/ckanext/toolsmetadata/lists/thematic_areas.txt")


# This Helper function creates the ftypesormats vocabulary from a text file
def createFormatsVocab():
     return createVocabulary("ILRI_vocformats","/opt/ckan-tools/ckan/src/ckanext-toolsmetadata/ckanext/toolsmetadata/lists/formats.txt")


# This Helper function creates the data types vocabulary from a text file
def createDataTypesVocab():
     return createVocabulary("ILRI_vocdatatypes","/opt/ckan-tools/ckan/src/ckanext-toolsmetadata/ckanext/toolsmetadata/lists/datatype.txt")
