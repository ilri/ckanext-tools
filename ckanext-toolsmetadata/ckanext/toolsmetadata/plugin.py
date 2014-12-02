import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from vocabularies import createSubjectsVocab
from vocabularies import createThemesVocab
from vocabularies import createFormatsVocab
from vocabularies import createDataTypesVocab

from utility import stringToTags
from utility import loadArray
from utility import valueInArray
from utility import valueInComaString
from utility import comaToArray

class toolsMetadataPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IDatasetForm, inherit=True)
    plugins.implements(plugins.IFacets)

    #Implements IConfigurer
    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_resource('resources', 'toolsMetadataResDir')

    #Implement  get_helpers of ITemplateHelpers
    def get_helpers(self):
        return {'toolsMetadata_createSubjectsVocab': createSubjectsVocab,
                'toolsMetadata_createThemesVocab': createThemesVocab,
                'toolsMetadata_createFormatsVocab': createFormatsVocab,
                'toolsMetadata_createDataTypesVocab': createDataTypesVocab,
                'toolsMetadata_loadArray': loadArray,
                'toolsMetadata_valueInArray': valueInArray,
                'toolsMetadata_valueInComaString': valueInComaString,
                'toolsMetadata_comaToArray': comaToArray
        }

    #Implements IDasetForm

    #Function that adds different fields to the schema when creating or updating a dataset
    def _add_custom_metadata_to_schema(self, schema):


        schema.update({'tool_website': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_contriborg': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_contact': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_contactemail': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_altcontact': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_altcontactemail': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})

        schema.update({'tool_subjects': [toolkit.get_validator('ignore_missing'),stringToTags]})
        schema.update({'tool_themes': [toolkit.get_validator('ignore_missing'),stringToTags]})
        schema.update({'tool_formats': [toolkit.get_validator('ignore_missing'),stringToTags]})

        schema.update({'tool_software': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_developer': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_language': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_year': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_lastupdate': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_personresp': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_source': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})

        schema.update({'tool_method': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_audiance': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_cycle': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_gender': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_spscale': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_orglevel': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})

        schema.update({'tool_datatypes': [toolkit.get_validator('ignore_missing'),stringToTags]})

        schema.update({'tool_datasource': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_output': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_assetype': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_guide': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})
        schema.update({'tool_citation': [toolkit.get_validator('ignore_missing'),toolkit.get_converter('convert_to_extras')]})

        return schema
    #
    #Function that adds different fields to the schema when showing the dataset
    def show_package_schema(self):
        schema = super(toolsMetadataPlugin, self).show_package_schema()

        # Don't show vocab tags mixed in with normal 'free' tags
        # (e.g. on dataset pages, or on the search page)

        schema['tags']['__extras'].append(toolkit.get_converter('free_tags_only'))

        schema.update({'tool_website': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_contriborg': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_contact': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_contactemail': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_altcontact': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_altcontactemail': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})

        schema.update({'tool_subjects': [toolkit.get_converter('convert_from_tags')("ILRI_vocsubjects"),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_themes': [toolkit.get_converter('convert_from_tags')("ILRI_vocthemes"),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_formats': [toolkit.get_converter('convert_from_tags')("ILRI_vocformats"),toolkit.get_validator('ignore_missing')]})

        schema.update({'tool_software': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_developer': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_language': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_year': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_lastupdate': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_personresp': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_source': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_method': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_audiance': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_cycle': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_gender': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_spscale': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_orglevel': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})

        schema.update({'tool_datatypes': [toolkit.get_converter('convert_from_tags')("ILRI_vocdatatypes"),toolkit.get_validator('ignore_missing')]})

        schema.update({'tool_datasource': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_output': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_assetype': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_guide': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})
        schema.update({'tool_citation': [toolkit.get_converter('convert_from_extras'),toolkit.get_validator('ignore_missing')]})

        return schema

    #Before the package is created add the fields to the model
    def create_package_schema(self):
        schema = super(toolsMetadataPlugin, self).create_package_schema()
        schema = self._add_custom_metadata_to_schema(schema)
        return schema

    #Before the package is updated add the fields to the model
    def update_package_schema(self):
        schema = super(toolsMetadataPlugin, self).update_package_schema()
        schema = self._add_custom_metadata_to_schema(schema)
        return schema

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    #Implement the neccesary fuctions of IDatasetForm
    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    #IFacets
    def dataset_facets(self,facets_dict, package_type):
        facets_dict['vocab_ILRI_vocsubjects'] = 'Subjects'
        facets_dict['vocab_ILRI_vocthemes'] = 'Themes'
        facets_dict['vocab_ILRI_vocformats'] = 'Tool Formats'
        facets_dict['vocab_ILRI_vocdatatypes'] = 'Data Types'
        return facets_dict

    def group_facets(self, facets_dict, group_type, package_type):
        facets_dict['vocab_ILRI_vocsubjects'] = 'Subjects'
        facets_dict['vocab_ILRI_vocthemes'] = 'Themes'
        facets_dict['vocab_ILRI_vocformats'] = 'Tool Formats'
        facets_dict['vocab_ILRI_vocdatatypes'] = 'Data Types'
        return facets_dict

    def organization_facets(self,facets_dict, organization_type, package_type):
        facets_dict['vocab_ILRI_vocsubjects'] = 'Subjects'
        facets_dict['vocab_ILRI_vocthemes'] = 'Themes'
        facets_dict['vocab_ILRI_vocformats'] = 'Tool Formats'
        facets_dict['vocab_ILRI_vocdatatypes'] = 'Data Types'
        return facets_dict;