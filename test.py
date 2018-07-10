import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FpO', "toing")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()


    def node_role(self):
        # remove existing node form the cluster
        # Check node_ip is internal or external
        node_role_list = []
        try:
            from kubernetes import client, config
            os.environ['KUBERNETES_SERVICE_HOST'] = 'kubernetes'
            config.load_incluster_config()
            core_v1 = client.CoreV1Api()
            nodes = core_v1.list_node()
            for node in nodes.items:
                node_metadata = {}
                for node_details in node.status.addresses:
                    if node_details.type == "InternalIP":
                        node_metadata[node_details.type] = node_details.address
                    if node_details.type == "Hostname":
                        node_metadata[node_details.type] = node_details.address
                if "nodetype" in node.metadata.labels:
                    role = node.metadata.labels.nodetype
                else:
                    role = "worker"
                node_metadata["role"] = role
                # kube join can only be initiated from private ip
                # node_metadata["privateIP"] = node_ip
                node_role_list.append(node_metadata)
        except Exception as exp:
            logger.error(str(exp))
        return node_role_list


    def get_node_role(self, hostname):
        node_list = self.node_role()
        role = None
        for node in node_list:
            if node["Hostname"] == hostname:
                role = node["role"]
        return role


    def get_master(self):
        node_list = self.node_role()
        master_metadata = {}
        for node in node_list:
            if node["role"] == "master":
                master_metadata = node
        return master_metadata


    def remove_node(self, master_ip, hostname):
        # TODO
        pass


    def cluster_join(self, master_ip, node_ip):
        error = ''
        try:
            url = ('http://' + master_ip + ':' + str(cp_deployment_port) +
                   '/cloudpoint/api/v3/kubejoin')

            logger.info("Sending join request to node: {0}".format(node_ip))
            body = {"master_ip": master_ip, "node_ip": node_ip}
            response = requests.post(url, json=body)
            response = response.json()
            if response.status_code not in range(200, 227):
                error_str = response.json()['errorMessage']
                error += ('Error adding node ' + node_ip + ' to ' +
                          'Kubernetes cluster ' + error_str + '\n')
        except Exception as exp:
            error += (str(exp))

        return {"error": error}


    def node_replacement(self, hostname, node_ip):
        role = self.get_node_role(hostname)
        master = self.get_master()
        master_ip = master["InternalIP"]
        if role == "worker":
            # do this
            # initiate_worker_join
            self.remove_node(master_ip, hostname)
            self.cluster_join(master_ip, node_ip)
        else:
            # if role is master do blah blah balh
            pass
