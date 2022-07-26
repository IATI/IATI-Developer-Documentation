import pytest


class TestSampleOutput:
    @pytest.mark.parametrize(
        ('file_path', 'expected_snippet'),
        [
            ("_build/dirhtml/index.html", "IATI Developer Documentation"),
        ]
    )
    def test_sample_output(self, file_path, expected_snippet):
        with open(file_path, "r") as open_file:
            file_contents = open_file.read()
            assert expected_snippet in file_contents