import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class toolsFrontEndPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    #IConfigurer

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public/images')
        toolkit.add_resource('resources', 'toolsFrontEndResDir')

