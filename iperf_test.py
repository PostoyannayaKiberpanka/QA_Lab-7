import parser


class TestSuite:
    def test_iperf3_client_connection(self, client):
        client_output, client_error = client

        assert client_error == '', f"Error in client execution: {client_error}"

        parsed_output = parser.parse_iperf_output(client_output)

        transfer_value = 20
        bitrate_value = 1.5

        assert float(parsed_output[
                         'Transfer']) > transfer_value, f"Transfer less than {transfer_value} MB: {parsed_output['Transfer']} MB"
        assert float(parsed_output[
                         'Bitrate']) > bitrate_value, f"Bitrate less than {bitrate_value} Gbits/s: {parsed_output['Bitrate']} Gbits/s"
