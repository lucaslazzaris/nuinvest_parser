from parser.note_parser import NoteParser

class TestNoteParser:
  def test_get_note_info(self, easynvesting_file):
    parser = NoteParser(easynvesting_file)
    note_info = parser.get_note_info()

    assert [
      [
        '24/08/2021',
        'IVVB11',
        'C',
        4,
        259.66,
        1038.94,
        'Easynvesting',
        '384268'
      ]
    ] == note_info

  def test_close_file(self, easynvesting_file):
    note_parser = NoteParser(easynvesting_file)
    note_parser.get_note_info()
    note_parser.close_file()

    assert note_parser.parser.fitz_file.is_closed