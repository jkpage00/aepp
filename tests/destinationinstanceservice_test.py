from aepp.destinationinstanceservice import DestinationInstanceService
import unittest
from unittest.mock import patch, MagicMock, ANY


class DestinationInstanceServiceTest(unittest.TestCase):

    @patch("aepp.connector.AdobeRequest")
    def test_create_adhoc_dataset_export(self, mock_connector):
        instance_conn = mock_connector.return_value
        instance_conn.postData.return_value = {'foo'}
        destination_instance_service_obj = DestinationInstanceService()
        result = destination_instance_service_obj.createAdHocDatasetExport({"flow1": ["dataset1"], "flow2": ["dataset2", "dataset3"]})
        assert(result is not None)
        instance_conn.postData.assert_called_once()
        instance_conn.postData.assert_called_with(ANY, data={'activationInfo': {'destinations': [{'flowId': 'flow1', 'datasets': [{'id': 'dataset1'}]}, {'flowId': 'flow2', 'datasets': [{'id': 'dataset2'}, {'id': 'dataset3'}]}]}})

    @patch("aepp.connector.AdobeRequest")
    def test_create_adhoc_dataset_export_invalid_input(self, mock_connector):
        destination_instance_service_obj = DestinationInstanceService()
        try:
            destination_instance_service_obj.createAdHocDatasetExport(None)
        except Exception as e:
            self.assertEqual(str(e), "Require a dict for defining the flowId to datasetIds mapping")
    