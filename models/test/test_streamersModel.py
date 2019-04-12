from unittest import mock, TestCase
from ..streamersModel import insertTopStreams

print(insertTopStreams)

class TestStreamersModel(TestCase):

  def test_patching_class(self):
    with mock.patch('streamersModel.insertTopStreams') as MockStreamers:
      MockStreamers.return_value.get_path.return_value = 'testing'
      worker = Worker()
      MockHelper.assert_called_once_with('db')
      self.assertEqual(worker.work(), 'testing')