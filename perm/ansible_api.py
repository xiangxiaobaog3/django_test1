# -*- coding: utf-8 -*-

from ansible.inventory.host import Host
from ansible.inventory.group import Group
from ansible.inventory import Inventory
from ansible.runner import Runner


class MyInventory(Inventory):
    """
    this is my ansible inventory object.
    """
    def __init__(self,resource):
        """
        resource的数据格式是一个列表字典
        :param resource:
        """
        self.resource = resource
        self.inventory = Inventory(host_list=[])
        self.gen_inventory()


    def my_add_group(self, host, groupname, groupvars=None):
        """
        add hosts to a group
        :param host:
        :param groupname:
        :param groupvars:
        :return:
        """
        my_group = Group(name=groupname)

        if groupvars:
            for key, value in groupvars.iteritems():
                my_group.set_variable(key, value)

        # add hosts to group
        for host in hosts:
            hostname = host.get("hostname")
            hostip = host.get('ip', hostname)
            hostport = host.get("port")
            username = host.get("username")
            password = host.get("password")
            ssh_key = host.get("ssh_key")
            my_host = Host(name=hostname, port=hostport)
            my_host.set_variable('ansible_ssh_ip', hostip)
            my_host.set_variable('ansible_ssh_port', hostport)
            my_host.set_variable('ansible_ssh_user', username)
            my_host.set_variable('ansible_ssh_pass', password)
            my_host.set_variable('ansible_private_key_file', ssh_key)

            # set other variables
            for key, value in host.iteritems():
                if key not in ["hostname", "port", "username", "password", "ip", "ssh_key"]:
                    my_host.set_variable(key, value)

            # add to group
            my_group.add_host(my_host)

        self.inventory.add_group(my_group)


    def gen_inventory(self):
        """
        add hosts to inventory
        :return:
        """
        if isinstance(self.resource, list):
            self.my_add_group(self.resource, 'default_group')
        elif isinstance(self.resource, dict):
            for groupname, host_and_vars in self.resource.iteritems():
                self.my_add_group(host_and_vars("hosts"), groupname, host_and_vars("vars"))

