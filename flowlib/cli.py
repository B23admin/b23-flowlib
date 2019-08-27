# -*- coding: utf-8 -*-
import argparse
import sys

import flowlib

class FlowLibConfig:
    def __init__(self, **kwargs):
        self.flow_yaml = kwargs.get('flow_yaml')
        self.export_yaml = kwargs.get('export_yaml')
        self.validate = kwargs.get('validate')
        self.scaffold = kwargs.get('scaffold')
        self.component_dir = kwargs.get('component_dir')
        self.nifi_endpoint = kwargs.get('nifi_endpoint')
        self.force = kwargs.get('force', False)

    def __repr__(self):
        return str(self.__dict__)


class FlowLibCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(prog="B23 FlowLib", description="A python library and cli for deploying NiFi flows from YAML")
        self.parser.add_argument('--version',
            action = 'version',
            version = '%(prog)s {}'.format(flowlib.__version__)
        )
        self.parser.add_argument('--nifi-endpoint',
            type = str,
            default = 'http://localhost:8080/nifi-api',
            help = 'A NiFi server endpoint'
        )
        self.parser.add_argument('--component-dir',
            type = str,
            help = 'A directory containing re-useable flowlib components'
        )
        self.parser.add_argument('--scaffold',
            type = str,
            help = 'Directory path to initialize with a new project scaffold'
        )
        self.parser.add_argument('--force',
            action = 'store_true',
            help = 'Force flowlib to overwrite an existing NiFi canvas'
        )
        # TODO: --flow-yaml should be required when validate is True
        self.parser.add_argument('--validate',
            action = 'store_true',
            help = 'Attempt to initialize the Flow from a flow.yaml by loading all of its components'
        )
        self.mx_group = self.parser.add_mutually_exclusive_group()
        self.mx_group.add_argument('--flow-yaml',
            type = argparse.FileType('r'),
            help = 'YAML file defining a NiFi flow to deploy'
        )
        self.mx_group.add_argument('--export-yaml',
            type = argparse.FileType('x'),
            help = 'Export the currently deployed NiFi flow as YAML. Prints to stdout if no filepath is specified'
        )
        self.config = FlowLibConfig(**vars(self.parser.parse_args()))
