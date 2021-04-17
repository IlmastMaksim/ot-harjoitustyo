from dearpygui.core import *
from dearpygui.simple import *

class Table:
    def __init__(self, name: str, header: List[str] = None):
        self.name = name
        self.header = header
        self.row = 0
        self.column = 0

        if header is not None:
            self.add_header(self.header)

    def add_header(self, header: List[str]):
        add_separator()
        with managed_columns(f"{self.name}_head", len(header)):
            for item in header:
                add_text(item)

    def add_row(self, row_content: List[Any]):
        with managed_columns(f"{self.name}_{self.row}", len(row_content)):
            for item in row_content:
                if type(item) is str:
                    add_input_text(f"##{self.name}_{self.row}_{self.column}", default_value=item, width=-1, height=50)
                self.column += 1
        self.column = 0
        self.row += 1
        add_separator()

    def get_cell_data(self, row: int, col: int) -> Any:
        return get_value(f"##{self.name}_{row}_{col}")