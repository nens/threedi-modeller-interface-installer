import os
import sys


if sys.version_info[0] == 2:
    import ConfigParser as configparser
else:
    import configparser

this_script_path =  os.path.dirname(__file__)


class QGISPluginBase(object):
    def __init__(self):
        self.__md_filename = os.path.join(
            this_script_path,
            "metadata.txt"
        )
        if not os.path.exists(self.__md_filename):
            raise ValueError("File metadata.txt not found")

        config = configparser.ConfigParser()
        config.read([self.__md_filename])

        self.__name = config.get('general', 'name').strip()
        self.__version = config.get('general', 'version')
        
        self.__pack_name = self.__generate_plugin_pack_name()

    @staticmethod
    def generate_metadata(plname):
        config = configparser.RawConfigParser()
        config.add_section('general')
        config.set('general', 'name', plname)

        config.set('general', 'qgisMinimumVersion', '')
        config.set('general', 'description', '')
        config.set('general', 'version', '')
        config.set('general', 'author', '')
        config.set('general', 'about', '')

        with open(os.path.join(this_script_path, 'metadata.txt'), 'w') as metafile:
            config.write(metafile)

    def __generate_plugin_pack_name(self):
        pl_dir_name = ""
        
        i = 0
        if ( self.__name.find(' ') > 0 ):
            while ( i < len(self.__name) ):
                if ( self.__name[i] == ' ' ):
                    while (self.__name[i] == ' ' ):
                        i += 1
                    pl_dir_name += '_'

                pl_dir_name += self.__name[i].lower()
                i += 1
        else:
            while ( i < len(self.__name) ):
                if ( self.__name[i].isupper() ):
                    pl_dir_name += '_'
                    while( self.__name[i].isupper() ):
                        pl_dir_name += self.__name[i].lower()
                        i += 1

                pl_dir_name += self.__name[i]
                i += 1

        return pl_dir_name.strip('_')
    
    @property
    def pack_name(self):
        return self.__pack_name
    
    @property
    def name(self):
        return self.__name

    @property
    def version(self):
        return self.__version

    @property
    def i18nPath(self):
        return os.path.join(this_script_path, "i18n")

    @property
    def dir(self):
        return this_script_path


if __name__ == "__main__":
    from qgis_plugin_framework.command_line import execute_manage_command
    execute_manage_command(QGISPluginBase(), sys.argv)
