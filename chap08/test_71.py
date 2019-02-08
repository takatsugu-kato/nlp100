import unittest
import nlp71

# 2.テストクラス名は「Testテスト対象のクラス名」とする
# 3.テストクラスはunittest.TestCaseを継承する
class TestCalc(unittest.TestCase):

  # 4.テストメソッド名は「test_テスト対象のメソッド名」とする(以下同)
  def test_hasStopWord(self):
    self.assertEqual(True, nlp71.isStopWord("the")) 
    self.assertEqual(True, nlp71.isStopWord("as"))
    self.assertEqual(True, nlp71.isStopWord("and"))
    self.assertEqual(False, nlp71.isStopWord("aaa"))
if __name__ == "__main__":
    unittest.main()